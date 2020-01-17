from indxprotoLib.hello import dl_hello_world
from indxprotoLib.dl_panda_frame import dl_panda_frame
from indxprotoLib.dl_panda_frame import dl_select_path_row
from indxprotoLib.dl_panda_frame import dl_generate_list_of_xmls

from c2indexLib.metadata_docs_bucket_xml import make_doc_from_meta_blob

import os
import boto3


def push_meta_to_elastic(bucketname, fpath):
    print(fpath)
    my_dir = os.path.dirname(fpath)
    meta_file_name = os.path.basename(fpath)
    print(my_dir, meta_file_name)
    meta_type = 'xml'
    s3 = boto3.resource('s3')
    replace_str = 's3://' + bucketname + '/'
    object_name = fpath.replace(replace_str, '')
    obj = s3.Object(bucketname, object_name)
    raw_string = obj.get()['Body'].read().decode('utf8')
    metadata_doc = make_doc_from_meta_blob(raw_string, meta_type, my_dir, meta_file_name)
    print(metadata_doc)


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

for fpath in paths:
    print(fpath)
    push_meta_to_elastic("dev-usgs-landsat", fpath)

