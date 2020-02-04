#! /bin/bash

for i in {2013..2019}; do
{
	echo $i
	python3 index_my_aoi.py -p 041 -r 035 -y $i l8
};
done
