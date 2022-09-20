# This file is for use as a .vscode devcontainer 
# The devcontainer should run as root and use podman or 
# docker with user namespaces.

FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    busybox \
    git \
    graphviz \
    net-tools \
    openssh-client \
    python3-pyqt5 \
    python3-venv \
    vim \
    x11-apps \
    && busybox --install


########## add podman and docker "outside" #####################################

# podman 4.2 has much better remote support than the ubuntu's apt repos version
RUN wget http://ftp.us.debian.org/debian/pool/main/libp/libpod/podman_4.2.0+ds1-3_amd64.deb && \
    apt install -y ./podman* && \
    rm podman*

# Point podman at the outside podman's user socket 
# This requires:
#   systemctl start podman.socket
#   podman -v /run/user/$(id -u)/podman/podman.sock:/podman.sock ...
# Works for docker clients too, as the socket inside is default docker one.
ENV CONTAINER_HOST="unix:/var/run/docker.sock"

# let docker clients find a docker-like cli if they need it
RUN ln -s /usr/bin/podman /usr/bin/docker


########## add python virtual environment ######################################

COPY dev_requirements.txt .

ENV VIRTUALENV=/venv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# install developer packages
RUN pip install -r dev_requirements.txt 
