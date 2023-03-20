# Selecionamos un imagen de Microsoft como nuestro base
FROM mcr.microsoft.com/devcontainers/python:0-3.11
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install git wget curl vim iputils-ping
RUN pip install -U pytest 