# This file is for use as a .vscode devcontainer 
# The devcontainer should run as root and use podman or 
# docker with user namespaces.

FROM python:3.10

# install additional packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    busybox \
    net-tools \
    python3-pyqt5 \
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && busybox --install

COPY dev_requirements.txt .

ENV VIRTUALENV=/venv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# install developer packages
RUN pip install -r dev_requirements.txt 


# add podman and docker inside / podman outside capabilities ###################

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    fuse-overlayfs \
    podman \
    && rm -rf /var/lib/apt/lists/*

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
# Point rootful podman at the default docker socket
ENV CONTAINER_HOST="unix:///var/run/docker.sock"
# Above means that you can: 
# enable a user socket to user podman with 'systemctl restart podman.socket'
# mount the socket with podman run options:
#   -v /run/user/$(id -u)/podman/podman.sock:/var/run/docker.sock
# Then container's docker and podman (-r) clients will see the user's host podman

# let docker clients find a docker cli if they need it
RUN ln -s /usr/bin/podman /usr/bin/docker
