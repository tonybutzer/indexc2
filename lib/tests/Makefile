runi:
	python3 index_nigeria_test.py
run:
	python3 test_xml.py

git:
	(cd /opt/indexc2; make)

initdb:
	datacube system init

product:
	datacube product add /opt/indexc2/product_definition/tony-nigeria-odc-product.yaml

all:	initdb product runi
