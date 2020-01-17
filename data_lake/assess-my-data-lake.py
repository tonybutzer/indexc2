# -*- coding: utf-8 -*-
""" assess-my-data-lake

    examines a bucket and prefix and creates a pandas frame for analyzing the area

    should be turned into a function in the library - soon

Examples:

        $ python assess-my-data-lake.py --bucket mubucket --prefix oli-tirs/2018


Todo:
    * make it a library

Code tells you how; Comments tell you why. -- Jeff Attwood

"""

import argparse
import boto3
import logging
import csv

def assess_bucket_prefix(bucket, prefix):
    """ creates a data frame from a bucket and prefix """
    print(bucket, prefix)

    print("ASSESS-"*44)

    fields=prefix.split('/')
    year=fields[4]

    data_file_name = 'analysis/' + bucket + '-' + year + '.csv';
    logging.info("Writing %s", data_file_name)
    data_file = open(data_file_name, mode='w')
    csv_writer=csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    cnt = 0
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    logging.info("Bucket : %s", bucket)
    for obj in bucket.objects.filter(Prefix=prefix):
        #print(obj.key)
        if obj.key.endswith('.xml') and not "aux" in obj.key:
            cnt = cnt + 1
            obj_key = obj.key
            logging.debug("Processing %s", obj_key)
            fields = obj_key.split('/')
            logging.debug("fields " + ",".join(fields))
            csv_writer.writerow(fields)

    logging.info("Counted %d Records!", cnt)
    data_file.close()


def mainfunc():
    """ analyzes a bucket and prefix as a pandas frame """

    logging.basicConfig(level=logging.INFO)

    p = argparse.ArgumentParser(description="parse some things.")

    p.add_argument("-b","--bucket")
    p.add_argument("-p","--prefix")

    opts = p.parse_args()

    print (opts)
    print (opts.bucket)
    print (opts.prefix)
    df = assess_bucket_prefix(opts.bucket, opts.prefix)


if __name__ == '__main__':
    mainfunc()
