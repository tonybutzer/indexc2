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

def return_meta_doc(bucketname, fpath):
    my_dir = os.path.dirname(fpath)
    meta_file_name = os.path.basename(fpath)
    meta_type = 'xml'
    s3 = boto3.resource('s3')
    replace_str = 's3://' + bucketname + '/'
    object_name = fpath.replace(replace_str, '')
    obj = s3.Object(bucketname, object_name)
    raw_string = obj.get()['Body'].read().decode('utf8')
    metadata_doc = make_doc_from_meta_blob(raw_string, meta_type, my_dir, meta_file_name)
    return (metadata_doc)

dl_hello_world()

path = "/opt/indexc2/data_lake/analysis"
pf = dl_panda_frame(path)

pf.columns = ['Collection', 'Level', 'Projection', 'Sensor', 'Year', 'Path', 'Row', 'Directory', 'XML_File']

print(pf.head())
print(pf.describe())


## do the whole lake this could take a while
paths = dl_generate_list_of_xmls("dev-usgs-landsat", pf)

meta_doc_list=[]
cnt = 0
for fpath in paths:
    cnt = cnt + 1
    if cnt % 200 == 0:
        print(cnt)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
    my_meta_doc = return_meta_doc("dev-usgs-landsat", fpath)
    meta_doc_list.append(my_meta_doc)

pickle.dump( meta_doc_list, open( "meta_docs_pickle.p", "wb" ) )

