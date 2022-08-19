# This file is for use as a .vscode devcontainer 
# The devcontainer should run as root and use podman or docker 
# with user namespaces.

FROM python:3.10

# install additional packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    busybox \
    git \
    net-tools \
    python3-pyqt5 \
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && busybox --install

COPY dev_requirements.txt .

ENV VIRTUALENV=/virtualenv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# install developer packages
RUN pip install --upgrade pip && \
    pip install -r dev_requirements.txt 
