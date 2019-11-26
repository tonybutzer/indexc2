FROM opendatacube/jupyter

USER root

RUN pip3 install ryd && pip install awscli && pip install eodatasets3

USER $NB_UID

WORKDIR /notebooks
