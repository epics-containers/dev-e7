# This file is for use as a .vscode devcontainer 
# The devcontainer should run as root and use podman or 
# docker with user namespaces.

FROM docker.io/python:3.10

########## add podman and docker inside / podman outside capabilities ##########

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    fuse-overlayfs \
    podman
 
# get default config files for containers and storage
ARG _URL="https://raw.githubusercontent.com/containers/podman/main/"
ADD $_URL/contrib/podmanimage/stable/containers.conf /etc/containers/containers.conf
ADD $_URL/vendor/github.com/containers/storage/storage.conf /usr/share/containers/storage.conf

# Copy default storage config and update for overlay fs
RUN sed -e 's|^#mount_program|mount_program|g' \
           -e '/additionalimage.*/a "/var/lib/shared",' \
           -e 's|^mountopt[[:space:]]*=.*$|mountopt = "nodev,fsync=0"|g' \
           /usr/share/containers/storage.conf \
           > /etc/containers/storage.conf

# container cache must me outside the container so no overlay on overlay
VOLUME /var/lib/containers
# put tmp outside of overlay filesystem for performance
VOLUME /tmp

# supply the lockfiles for the container filesystems
RUN mkdir -p /var/lib/shared/overlay-images \
             /var/lib/shared/overlay-layers \
             /var/lib/shared/vfs-images \
             /var/lib/shared/vfs-layers && \
    touch /var/lib/shared/overlay-images/images.lock && \
    touch /var/lib/shared/overlay-layers/layers.lock && \
    touch /var/lib/shared/vfs-images/images.lock && \
    touch /var/lib/shared/vfs-layers/layers.lock

ENV _CONTAINERS_USERNS_CONFIGURED=""

# Point remote podman at the outside podman's user socket
# This requires:
#   systemctl restart podman.socket
#   podman -v /run/user/$(id -u)/podman/podman.sock:/podman.sock ...
ENV CONTAINER_HOST="unix:/podman.sock"

# let docker clients find a docker-like cli if they need it
RUN ln -s /usr/bin/podman /usr/bin/docker

# add script to start podman service for serving docker clients
COPY podman_service /usr/bin
RUN chmod +x /usr/bin/podman_service

########## podman and docker done ##############################################

# install additional packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    busybox \
    graphviz \
    net-tools \
    python3-pyqt5 \
    vim \
    x11-apps \
    && busybox --install

COPY dev_requirements.txt .

ENV VIRTUALENV=/venv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# install developer packages
RUN pip install -r dev_requirements.txt 
