FROM opendatacube/jupyter

USER root

RUN pip3 install ryd && pip install awscli && pip install eodatasets3

RUN apt-get update && apt-get install -y vim

USER $NB_UID

WORKDIR /notebooks
