# indexc2
collate index python code for populating an ODC postgresdb from L2 Landsat
- C2-provisional data   ## eventually the real Collection 2
- C1-L2-Albers-Scenes

# HOWTO Run and Test Indexing

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
