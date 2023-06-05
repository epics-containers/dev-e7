
# This file is for use as a .vscode devcontainer
# The devcontainer should run as root and use user-mode podman or
# docker with user namespaces.

FROM ubuntu:22.04

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get upgrade -y && \
    apt-get install -yq --no-install-recommends \
    apt-file \
    apt-transport-https \
    autossh \
    build-essential \
    busybox \
    ca-certificates \
    curl \
    git \
    gnupg \
    graphviz \
    net-tools \
    openssh-client \
    python3-dev \
    python3-pyqt5 \
    python3-venv \
    rsync \
    software-properties-common \
    vim \
    x11-apps \
    && add-apt-repository ppa:deadsnakes/ppa \
    && busybox --install

ARG TARGETARCH
ENV TARGETARCH=${TARGETARCH}

########## add kubernetes cli tools ############################################

# kubectl
RUN echo target architecture is ${TARGETARCH} && \
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/${TARGETARCH}/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# helm
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
     ./get_helm.sh

# oidc-login
RUN curl -L "https://github.com/int128/kubelogin/releases/download/v1.27.0/kubelogin_linux_${TARGETARCH}.zip" --output /tmp/kubelogin.zip && \
    unzip /tmp/kubelogin.zip kubelogin && \
    mv kubelogin /usr/local/bin/kubectl-oidc_login

########## docker client #######################################################

# Here we install the docker CLI only with the intention of using it to connect
# to the host's docker or podman daemon.

# If you are running podman on the host, you can use the host's podman as follows:
# Enable a user podman service (once only):
#   systemctl enable --user podman.socket
#   systemctl start --user podman.socket
# Launch the devcontainer with the host's podman socket mounted:
#   podman run -it -v=${XDG_RUNTIME_DIR}/podman/podman.sock:/var/run/docker.sock --security-opt=label=disable ghcr.io/epics-containers/dev-e7:latest
#
# If you are running docker on the host, you can use the host's docker as follows:
#   docker run -it -v=/var/run/docker.sock:/var/run/docker.sock --security-opt=label=disable ghcr.io/epics-containers/dev-e7:latest

# install docker cli
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    # NOTE not installing latest to avoid build deprecation warning
    # for review - how to keep podman-from-docker working once docker build is removed?
    # even docker-from-docker has challenges once this happens I believe.
    # This has been tested with podman on the host and docker-ce-cli version
    # 5:20.10.24~3-0~ubuntu-jammy which works but gives deprecation warning on build.
    apt-get install  -yq --no-install-recommends docker-ce-cli==5:20.10.24~3-0~ubuntu-jammy

# let podman clients find a podman-like cli if they need it (e.g. ec)
RUN ln -s /usr/bin/docker /usr/bin/podman

########## environment #########################################################

# disable buildkit as podman does not yet support it
ENV DOCKER_BUILDKIT=0
# add a prompt to indicate we are in the e7 dev container
ENV DEV_PROMPT=E7


######### Add in EPICS 7 tools and build environ ###############################

ENV EPICS_ROOT=/repos/epics
ENV EPICS_BASE=${EPICS_ROOT}/epics-base
ENV EPICS_HOST_ARCH=linux-x86_64
ENV PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

COPY --from=ghcr.io/epics-containers/epics-base-linux-developer:23.2.1 ${EPICS_BASE} ${EPICS_BASE}

######### Misc Tools ###########################################################

# add pie (python install editable) script in the path
COPY pie /usr/local/bin/pie

######### Python 3.10 and packages to support epics-containers ################

RUN git config --global pull.rebase false

ENV PYTHON_VERSION 3.10
ENV VIRTUALENV=/venv

# install required python version from deadsnakes if needed
# uncomment below when not using python3.10 (which is default for ubuntu 22.04)
# RUN DEBIAN_FRONTEND=noninteractive \
#     apt-get -y install python${PYTHON_VERSION} python${PYTHON_VERSION}-venv

# set up a global virtual environ for all projects in the container
RUN python${PYTHON_VERSION} -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:$PATH

# make sure we have the latest pip
RUN pip install --upgrade pip
# install epics containers python tools
RUN pip install python3-pip-skeleton[dev] epics-containers-cli>=0.4

