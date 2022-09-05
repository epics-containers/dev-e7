# This file is for use as a .vscode devcontainer 
# The devcontainer should run as root and use podman or docker 
# with user namespaces.
#
# It also can be run standalone with podman or docker.

FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.10-bullseye

# install additional packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    net-tools \
    python3-pyqt5 \
    vim \
    && rm -rf /var/lib/apt/lists/* 

COPY dev_requirements.txt .

ENV VIRTUALENV=/virtualenv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# install developer packages
RUN pip install --upgrade pip && \
    pip install -r dev_requirements.txt 

### BELOW ADDS DOCKER IN PODMAN/DOCKER SUPPORT #################################

# These options enable docker in podman
# podman run --rm -it --cap-add=sys_admin,mknod,net_admin --device=/dev/fuse --security-opt=label=type:container_runtime_t IMAGE_NAME bash
# OR
# podman run --rm -it --privileged IMAGE_NAME bash

# use vscode script to enable docker inside this container
# modify the deamon script to disbale iptables in dockerd (for DLS compatibilty)
ENV DOCKERD_OPT="--iptables=false"
RUN wget https://raw.githubusercontent.com/microsoft/vscode-dev-containers/main/script-library/docker-in-docker-debian.sh && \
    bash docker-in-docker-debian.sh && \
    sed -i 's/dockerd $CUSTOMDNS/dockerd $DOCKERD_OPT $CUSTOMDNS/' /usr/local/share/docker-init.sh

# docker's overlay filesystem must exist outside of the container
VOLUME [ "/var/lib/docker" ]
# this starts the docker daemon, then executes the command passed to the podman run
ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]

### BELOW ADDS PODMAN OUTSIDE PODMAN SUPPORT ###################################

# to enable this you need to run a podman user service on the host:
# systemctl --user status podman.socket
# and mount the podman socket into the container:
# podman run --rm -it --privileged -v /run/user/$(id -u)/podman/podman.sock:/run/podman/podman.sock IMAGE_NAME bash

RUN docker context create podman --docker "host=unix:///run/podman/podman.sock" && \
    echo 'docker --context podman "$@"' > /usr/local/bin/podman && \
    chmod +x /usr/local/bin/podman



