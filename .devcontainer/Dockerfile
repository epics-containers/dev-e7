# This file is for use as a .vscode devcontainer 
# The devcontainer should run as root and use podman or docker 
# with user namespaces.

FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.10-bullseye

# install additional packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    net-tools \
    python3-pyqt5 \
    && rm -rf /var/lib/apt/lists/*

COPY dev_requirements.txt .

ENV VIRTUALENV=/virtualenv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# install developer packages
RUN pip install --upgrade pip && \
    pip install -r dev_requirements.txt 

# add the docker cli only (for driving the host podman)
RUN docker_url=https://download.docker.com/linux/static/stable/x86_64 && \
    docker_version=20.10.9 && \
    curl -fsSL $docker_url/docker-$docker_version.tgz | \
    tar zxvf - --strip 1 -C /usr/bin docker/docker

# opionated shell prompt which shows which container you are in
# RUN bash -c "curl -sS https://starship.rs/install.sh | sh -s -- -y"
