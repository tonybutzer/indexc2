"""
creates a bucnh of csv files one per path

stores them in analysis
"""

import logging
import boto3
import csv
import re
# from multiprocessing import Process, current_process, Queue, Manager, cpu_count
# import threading

print("hello csv files")

def path_list(file):
    pl = []
    with open(file) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            line=line.strip()
            line = re.sub(r'^.*PRE ','', line)
            line = re.sub(r'/.*$','', line)
            #print("Line {}: {}".format(cnt, line.strip()))
            pl.append(line)
            line = fp.readline()
            cnt += 1
    return pl

def worker(path):
    """ creates a csv files a bucket and prefix """
    print ("WORKER",path)

    bucket = 'deafrica-usgs-c2-data'
    prefix = 'usgs_ls8c_level2_2/' + path
    print(bucket, prefix)

    data_file_name = 'analysis/' + bucket + '-' + path + '.csv';
    logging.info("Writing %s", data_file_name)
    data_file = open(data_file_name, mode='w')
    csv_writer=csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    cnt = 0
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    logging.info("Bucket : %s", bucket)
    for obj in bucket.objects.filter(Prefix=prefix):
        #print(obj.key)
        if obj.key.endswith('.odc-metadata.yaml'):
            cnt = cnt + 1
            obj_key = obj.key
            logging.debug("Processing %s", obj_key)
            fields = obj_key.split('/')
            logging.debug("fields " + ",".join(fields))
            csv_writer.writerow(fields)

    logging.info("Counted %d Records!", cnt)
    data_file.close()



def mainfunc():

    logging.basicConfig(level=logging.INFO)

    paths = []
    paths = path_list('./paths.txt')
    print(len(paths))
    jobs = []

    # Create a list of jobs  one for each path and then iterate through
    # the number of threads appending each thread to
    # the job list
    for i in range(0, len(paths)):
        worker(paths[i])

    print("Create csv done")




mainfunc()
