FROM opendatacube/jupyter

USER root

RUN pip3 install ryd && pip install awscli && pip install eodatasets3

RUN apt-get update && apt-get install -y vim

ENV tversion=2.0
RUN (cd /opt ; git clone http://github.com/tonybutzer/indexc2) \
	&& (cd /opt/indexc2/lib; make build-root)

USER $NB_UID

WORKDIR /notebooks
