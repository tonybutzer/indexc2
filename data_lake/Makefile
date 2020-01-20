echo:
	echo hi 

assess:
	# (export PAGER=cat; pydoc assess-my-data-lake)
	python3 assess-my-data-lake.py --bucket dev-usgs-landsat --prefix collection1/level2/albers/oli-tirs/2013/
	# python3 assess-my-data-lake.py --bucket dev-usgs-landsat --prefix collection1/level2/albers/oli-tirs/2018/046/028/



test-panda:
	echo "should be run in cube in a box"
	python3 test_panda_data_lake.py

pickle:
	echo "should be run in cube in a box"
	python3 pickle_panda_data_lake.py


git:
	(cd /opt/indexc2; make)

