from indxprotoLib.hello import dl_hello_world
from indxprotoLib.dl_panda_frame import dl_panda_frame
from indxprotoLib.dl_panda_frame import dl_select_path_row
from indxprotoLib.dl_panda_frame import dl_generate_list_of_xmls

from c2indexLib.metadata_docs_bucket_xml import make_doc_from_meta_blob
from c2indexLib.elastic_index import store_record
from c2indexLib.elastic_meta import elastic_flatten_doc
from c2indexLib.elastic_index import connect_elasticsearch
from c2indexLib.elastic_index import l_create_index


import os
import boto3
import json
import pprint
from datetime import datetime
import pickle

def create_elastic_connection_and_index():
    es_conn = connect_elasticsearch()
    # delete any old indexes - similar to clearing the postgres db
    es_conn.indices.delete(index='datalake', ignore=[400, 404])

    # create new elastic search index
    index_name='datalake'
    record_type = 'odclite'
    l_create_index(es_conn, index_name, record_type)

    return es_conn


def push_meta_to_elastic(bucketname, fpath):
    # print(fpath)
    my_dir = os.path.dirname(fpath)
    meta_file_name = os.path.basename(fpath)
    # print(my_dir, meta_file_name)
    meta_type = 'xml'
    s3 = boto3.resource('s3')
    replace_str = 's3://' + bucketname + '/'
    object_name = fpath.replace(replace_str, '')
    obj = s3.Object(bucketname, object_name)
    raw_string = obj.get()['Body'].read().decode('utf8')
    metadata_doc = make_doc_from_meta_blob(raw_string, meta_type, my_dir, meta_file_name)
    # print(metadata_doc)
    elastic_ready_doc = elastic_flatten_doc(metadata_doc)
    elastic_json_record = json.dumps(elastic_ready_doc)
    # print("###"*30)
    # pprint.pprint(elastic_json_record)
    index_name='datalake'
    record_type = 'odclite'
    store_record(es_conn, index_name, record_type, elastic_json_record)
    return (elastic_json_record)



dl_hello_world()

path = "/opt/indexc2/data_lake/analysis"
pf = dl_panda_frame(path)

pf.columns = ['Collection', 'Level', 'Projection', 'Sensor', 'Year', 'Path', 'Row', 'Directory', 'XML_File']

print(pf.head())
print(pf.describe())

path = '046'
row = '028'
aoi_pf = dl_select_path_row(pf, path, row)

print(aoi_pf.head())
print(aoi_pf.describe())

paths = dl_generate_list_of_xmls("dev-usgs-landsat", aoi_pf)

## do the whole lake this could take a while
## paths = dl_generate_list_of_xmls("dev-usgs-landsat", pf)

es_conn = create_elastic_connection_and_index()

meta_doc_list=[]
cnt = 0
for fpath in paths:
    cnt = cnt + 1
    if cnt % 200 == 0:
        print(cnt)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
    my_meta_doc = push_meta_to_elastic("dev-usgs-landsat", fpath)
    meta_doc_list.append(my_meta_doc)

pickle.dump( meta_doc_list, open( "/notebooks/opt/meta_docs_elastic_json_pickle.p", "wb" ) )

