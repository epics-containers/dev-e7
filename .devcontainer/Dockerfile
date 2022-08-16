# ideas from https://www.docker.com/blog/containerized-python-development-part-1/

# This file is for use as a .vscode devcontainer as well as a runtime 
# container. The devcontainer should be rootful and use podman or docker 
# with user namespaces.

FROM python:3.10 as base

# use root to pin where the packages will install
USER root
ENV PYTHONPREFIX=/python
ENV PATH=${PYTHONPREFIX}/bin:$PATH
ENV PYTHONPATH=${PYTHONPREFIX}

# install additional packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-pyqt5 \
    && rm -rf /var/lib/apt/lists/*

FROM base as developer

COPY . .

# install deveoloper packages
RUN mkdir -p ${PYTHONPREFIX} && \
    pip install --upgrade pip && \
    pip install --prefix ${PYTHONPREFIX} -r dev_requirements.txt 

FROM base as runtime

COPY --from=developer ${PYTHONPREFIX} ${PYTHONPREFIX}

