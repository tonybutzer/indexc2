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


initdbc2:
	datacube system init --no-init-users

metadatac2:
	datacube metadata add https://github.com/digitalearthafrica/config/raw/usgs-collection2/products/eo3_landsat_ard.odc-type.yaml

productc2:
	datacube product add https://github.com/digitalearthafrica/config/raw/usgs-collection2/products/usgs-level2-collection2-sample.odc-product.yaml

indexc2:
	s3-find s3://deafrica-usgs-c2-data/usgs_ls8c_level2_2/157/*/*/*/*/*.yaml | s3-to-tar >a.tar
	dc-index-from-tar --e03 < a.tar

allc2:	initdbc2 metadatac2 productc2 indexc2

git:
	(cd /opt/indexc2; make)

