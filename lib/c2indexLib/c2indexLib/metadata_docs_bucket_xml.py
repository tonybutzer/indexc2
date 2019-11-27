"""
metadata_docs_bucket_xml.py

Used in Open Data Cube Preparei/Indexing Scripts
and as always seems to be a Work in Progress -- WIP!
Testing this with local USB Drive Data over Rwanda
This script crawls a rwanda director of &*.xml files
* 1. locates the xml metadata
* 2. creates a gneric metaBlob from xml (could be done for json or MTL) blob for each metadata file
* 3. loads these into the postgresql database as a JSONB blob object - using odc dc routine:
    add_dataset(...):
"""

import boto3
import logging
import os

def wtf():
    print ("wtf"*33)

def get_metadata_docs_bucket_xml(bucket_name, prefix):

    print("hello-"*44)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    logging.info("Bucket : %s", bucket_name)
    for obj in bucket.objects.filter(Prefix=prefix):
        #print(obj.key)
        if obj.key.endswith('.xml') and not "aux" in obj.key:
            obj_key = obj.key
            logging.info("Processing %s", obj_key)
            raw_string = obj.get()['Body'].read().decode('utf8')
            # print(raw_string)
            meta_type = 'xml'
            dir_name=prefix
            meta_file_name=obj_key
            print("DIRNAME:", dir_name, "META:", meta_file_name)
            my_dir = dir_name = os.path.dirname(meta_file_name)
            print("MYDIR:", my_dir, "META:", meta_file_name)
            my_dir = "s3://" + bucket_name + '/'  + my_dir

            #metadata_doc = make_doc_from_meta_blob(raw_string, meta_type, my_dir, meta_file_name)
            #metadata_doc = make_xml_doc(raw_string,bucket_name, obj_key)
            # print(metadata_doc)
            # TONY
            #yield obj_key, metadata_doc
