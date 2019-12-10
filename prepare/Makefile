runi:
	python3 index_hayden.py

git:
	(cd /opt/indexc2; make)

initdb:
	datacube system init

product:
	datacube product add /opt/indexc2/product_definition/l2-odc-product.yaml

drop:
	./dropDatabaseTables.sh

all:	initdb product runi
