# This file is for use as a .vscode devcontainer 
# The devcontainer should run as root and use podman or 
# docker with user namespaces.

FROM python:3.10

# install additional packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    busybox \
    git \
    net-tools \
    python3-pyqt5 \
    python3-pip \
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && busybox --install

COPY dev_requirements.txt .

ENV VIRTUALENV=/venv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# install developer packages
RUN pip install -r dev_requirements.txt 

# add the docker cli only (for driving the host podman)
RUN docker_url=https://download.docker.com/linux/static/stable/x86_64 && \
    docker_version=20.10.9 && \
    curl -fsSL $docker_url/docker-$docker_version.tgz | \
    tar zxvf - --strip 1 -C /usr/bin docker/docker

# opionated shell prompt which shows which container you are in
# RUN bash -c "curl -sS https://starship.rs/install.sh | sh -s -- -y"
