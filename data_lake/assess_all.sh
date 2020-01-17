#! /bin/bash

for i in {2013..2020}; \
        do echo $i; \
       	python3 assess-my-data-lake.py --bucket dev-usgs-landsat \
	--prefix collection1/level2/albers/oli-tirs/${i} ; \
	done
