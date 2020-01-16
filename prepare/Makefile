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





git:
	(cd /opt/indexc2; make)

