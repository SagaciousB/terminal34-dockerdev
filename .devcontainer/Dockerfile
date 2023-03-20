# Selecionamos una imagen de Microsoft como nuestro base
FROM mcr.microsoft.com/devcontainers/python:0-3.11

# Añadir unas cosas importantes por mi proyecto con apt
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install git wget curl vim iputils-ping

# Y unos paquetes de pip
RUN pip install -U pytest numpy