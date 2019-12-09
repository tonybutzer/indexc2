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
import uuid

from c2indexLib.meta_blob_from_xml import MetaBlob

from c2indexLib.satellite_ref import satellite_ref
from c2indexLib.satellite_ref import get_band_file_map
from c2indexLib.projection_stuff import get_projection_info


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

    ####
    level = meta_blob.product_id.split('_')[1]
    images, product_type = satellite_ref(meta_blob.satellite)
    print("IMAGES",images)
    center_dt = meta_blob.acquisition_date + " " + meta_blob.scene_center_time
    start_time = center_dt
    end_time = center_dt

    #####

    print(meta_blob.band_dict)
    # print("FILE_NAME_BAND_4: ", meta_blob.band_dict['FILE_NAME_BAND_4'])

    #geo_guinea_pig = meta_blob.band_dict['FILE_NAME_BAND_4']

    # spatial_ref = get_projection_info(geo_guinea_pig)

    # TONY FIX this HARDCODE soon!

    spatial_ref = 'epsg:5072'
    #spatial_ref = 'epsg:32631'

    #####

    westxf = float(meta_blob.westx) * 1.0
    eastxf = float(meta_blob.eastx) * 1.0
    northyf = float(meta_blob.northy) * 1.0
    southyf = float(meta_blob.southy) * 1.0

    geo_ref_points = {
          'ul':
             {'x': westxf,
              'y': northyf},
          'ur':
             {'x': eastxf,
              'y': northyf},
          'lr':
             {'x': eastxf,
              'y': southyf},
          'll':
             {'x': westxf,
              'y': southyf}}

    print("COORD=", meta_blob.coord)
    print("UPPER_LEFT=", geo_ref_points['ul'])
    docdict = {
        'id': str(uuid.uuid4()),
        'processing_level': str(level),
        'product_type': product_type,
        'creation_dt': meta_blob.acquisition_date,
        'platform': {'code': meta_blob.satellite},
        'instrument': {'name': meta_blob.instrument},
        'extent': {
            'from_dt': str(start_time),
            'to_dt': str(end_time),
            'center_dt': str(center_dt),
            'coord': meta_blob.coord,
        },
        'format': {'name': 'GeoTiff'},

        'grid_spatial': {
            'projection': {
                'geo_ref_points': geo_ref_points,
                'spatial_reference': spatial_ref,
            }
        },
        'image': {
            'bands': {
                image[1]: {
                    'path': meta_blob.band_dict[get_band_file_map(image[1])],
                    'layer': 1,
                } for image in images
            }
        },

        'lineage': {'source_datasets': {}}
    }
    print (docdict)
    return docdict



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
            yield obj_key, metadata_doc
