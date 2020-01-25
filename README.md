# indexc2
collate index python code for populating an ODC postgresdb from L2 Landsat
- C2-provisional data   ## eventually the real Collection 2
- C1-L2-Albers-Scenes

## INDEX C2 Africa from existing yamls

```
cd /opt/indexc2/ciabidx

make down

make build-just-indexc2

make up

make exec

cd /opt/indexc2/prepare

make all
```

test with notebook of bolama


# HOWTO Run and Test Indexing

## Collection 2 Nigeria

```
TBD
```

## C1-L2-Albers-Scenes USGS CHS ONLY

```
cd ciabidx
make up
make init-db

make exec

make all   # initdb;  make product and run hayden index

```
## Then jupyter
```
ssh tunnel 8888 ~/bin/01-tunnel...

firefox localhost:8888

cd 00-notebooks

00-hayden-progress # restart and run all
```

1. cube-in-a-box deployment
    - postgresql
     - odc/jupyter # need to customize
    - add elastic and kibana
    - add libraries and repos
        - lite-stac library
        - notebook repo and tests

## DataLake
1. C1-L2-Albers

## Approaches

1. modify dcindexLib
2. use cube-in-a-box examples
3. use eodatasets3 - uses yaml - likely overcomplicates these limited flows

none of these are simple :-(

## Today

1. practice and document indexing and clearing and testing the database
2. cleanup Makefiles

## WIP

1. User Interface - improve with click
2. Optional Elastic Viewing
3. Improve cube-in-the-box with elastic in this repo for testing
4. Move hayden activities to notebook
5. map out dependency tree

## Failed WIP

1. disect eodatasets3 from
	- https://github.com/GeoscienceAustralia/eo-datasets
