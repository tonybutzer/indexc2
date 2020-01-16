echo:
	echo hi 

all:	initdb product runi

initdb:
	datacube system init

product:
	datacube product add /opt/indexc2/product_definition/c1-l2-albers-scene-odc-product.yaml

runi:
	python3 index_hayden_c1l2_albers_scene.py

drop:
	./dropDatabaseTables.sh


assess:
	# (export PAGER=cat; pydoc assess-my-data-lake)
	python3 assess-my-data-lake.py --bucket dev-usgs-landsat --prefix collection1/level2/albers/oli-tirs/2013/
	# python3 assess-my-data-lake.py --bucket dev-usgs-landsat --prefix collection1/level2/albers/oli-tirs/2018/046/028/





git:
	(cd /opt/indexc2; make)

