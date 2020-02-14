echo:
	echo hi 

all:	initdb product runi sanath

initdb:
	datacube system init

product:
	datacube product add /opt/indexc2/product_definition/c1-l2-albers-scene-odc-product.yaml

runi:
	python3 index_hayden_c1l2_albers_scene.py

sanath:
	./ip041r035.sh

drop:
	./dropDatabaseTables.sh


initdbc2:
	datacube system init --no-init-users

metadatac2:
	datacube metadata add https://raw.githubusercontent.com/digitalearthafrica/config/ows-refactor/products/eo3_landsat_ard.odc-type.yaml

productc2:
	datacube product add https://raw.githubusercontent.com/digitalearthafrica/config/ows-refactor/products/usgs-level2-collection2-sample.odc-product.yaml

indexc2:
	s3-find s3://deafrica-usgs-c2-data/usgs_ls8c_level2_2/204/*/*/*/*/*.odc-metadata.yaml | s3-to-tar >/notebooks/p204.tar
	dc-index-from-tar --eo3 < /notebooks/p204.tar

allc2:	initdbc2 metadatac2 productc2 indexc2

git:
	(cd /opt/indexc2; make)

