get-geomedians:
	wget https://raw.githubusercontent.com/GeoscienceAustralia/digitalearthau/config-geomedian/digitalearthau/config/cambodia/geomed_product.yaml -O data/geomed_product.yaml
	wget http://dea-public-data.s3-ap-southeast-2.amazonaws.com/ewater/cambodia_cube/output_2014/ls_level2/ls_level2_nbart_26_39_20140101.tif -O data/ls_level2_nbart_26_39_20140101.tif
	wget http://dea-public-data.s3-ap-southeast-2.amazonaws.com/ewater/cambodia_cube/output_2014/ls_level2/ls_level2_nbart_26_39_20140101.yaml -O data/ls_level2_nbart_26_39_20140101.yaml

get-indexer:
	wget https://raw.githubusercontent.com/opendatacube/datacube-ecs/geomedian/indexer/ls_s2_cog.py -O data/ls_s3_cog.py
	chmod +x data/ls_s2_cog.py

up:
	docker-compose up

build:
	docker-compose build

exec:
	docker-compose exec jupyter bash

init-db:
	docker-compose exec jupyter datacube system init

make-products:
	docker-compose exec jupyter datacube product add /notebooks/geomed_product.yaml

index:
	docker-compose exec jupyter datacube dataset add /notebooks/ls_level2_nbart_26_39_20140101.yaml
	# docker-compose exec jupyter \
	# 	python3 /notebooks/ls_s3_cog.py \
	# 		dea-public-data \
	# 		--prefix ewater/cambodia_cube/output_2014/ls_level2/ \
	# 		--unsafe


# http://dea-public-data.s3-website-ap-southeast-2.amazonaws.com/?prefix=ewater/cambodia_cube/output_2014/ls_level2/


test-elastic:
	docker-compose exec kibana curl elasticsearch:9200

test-index-lib:
	docker-compose exec jupyter python3 /opt/indexc2/lib/tests/test_xml.py


git:
	(cd /opt/indexc2 ; make)
