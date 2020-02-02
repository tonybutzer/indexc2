import logging
import json
import pprint
import datacube

from c2indexLib.metadata_docs_bucket_xml import get_metadata_docs_bucket_xml
from c2indexLib.elastic_meta import elastic_flatten_doc
from c2indexLib.elastic_index import connect_elasticsearch
from c2indexLib.elastic_index import l_create_index
from c2indexLib.elastic_index import store_record

from c2indexLib.datacube_index import add_dataset

def index_records(path,row,year):
    bucket = "dev-usgs-landsat"

    #prefix = "collection1/level2/albers/oli-tirs/2014/041/035/"
    prefix = 'collection1/level2/albers/oli-tirs/' + year + '/' + path + '/' + row + '/'

    cnt=0
    print ("meta loop")

    # ELASTIC=False
    ELASTIC=True
    
    cnt=0;

    es_conn = connect_elasticsearch()


    # delete any old indexes - similar to clearing the postgres db
    if ELASTIC:
        es_conn.indices.delete(index='cube', ignore=[400, 404])

    # create new elastic search index
    if ELASTIC:
        index_name='cube'
        record_type = 'odclite'
        l_create_index(es_conn, index_name, record_type)

    # create datacube index postgres
    config='.datacube.conf'
    dc = datacube.Datacube(config=config)
    index = dc.index
    source_policy = 'skip'

    for metadata_path, metadata_doc in get_metadata_docs_bucket_xml(bucket, prefix):
        uri = metadata_path
        print(uri)
        cnt=cnt+1
        print(cnt)
        print("INDEXER META:", metadata_doc)
        elastic_ready_doc = elastic_flatten_doc(metadata_doc)
        logging.info("Indexing %s", metadata_path)
        add_dataset(metadata_doc, uri, index, source_policy)
        print("creationdate", metadata_doc['creation_dt'])
        print(elastic_ready_doc)
        elastic_json_record = json.dumps(elastic_ready_doc)
        print("###"*30)
        pprint.pprint(elastic_json_record)
        if ELASTIC:
            store_record(es_conn, index_name, record_type, elastic_json_record)

