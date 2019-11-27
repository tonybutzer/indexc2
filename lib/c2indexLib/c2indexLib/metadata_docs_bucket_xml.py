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

from c2indexLib.meta_blob_from_xml import MetaBlob


def get_xml_string(file):
    """ read xml into memory from xml_meta_file """

    with open(file, 'r') as content_file:
        content = content_file.read()
    # print (content)
    return content

def make_doc_from_meta_blob(xml_string, type, directory, meta_file_name):
    """ just does xml for now - need to add MTL and json """
    logging.info("\nMeta Blob %s", meta_file_name)
    if xml_string is None:
        xml_raw = get_xml_string(meta_file_name)
    else:
        xml_raw = xml_string
    meta_blob = MetaBlob(directory, xml_raw)
    meta_blob.get_global_metadata()


def get_metadata_docs_bucket_xml(bucket_name, prefix):

    print("hello-"*44)

    cnt = 0
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    logging.info("Bucket : %s", bucket_name)
    for obj in bucket.objects.filter(Prefix=prefix):
        #print(obj.key)
        if obj.key.endswith('.xml') and not "aux" in obj.key:
            cnt = cnt + 1
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

            metadata_doc = make_doc_from_meta_blob(raw_string, meta_type, my_dir, meta_file_name)
            print(metadata_doc)
            print(cnt)
            #yield obj_key, metadata_doc
