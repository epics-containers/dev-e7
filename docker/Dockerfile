
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

########## environment #########################################################

ENV DEV_PROMPT=E7


######### Add in EPICS 7 tools and build environ ###############################

# ENV EPICS_ROOT=/repos/epics
# ENV EPICS_BASE=${EPICS_ROOT}/epics-base
# ENV EPICS_HOST_ARCH=linux-x86_64
# ENV PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

# COPY --from=ghcr.io/epics-containers/epics-base-linux-developer:23.2.1 ${EPICS_BASE} ${EPICS_BASE}

######### Misc Tools ###########################################################

# add pie (python install editable) script in the path
COPY pie /usr/local/bin/pie

RUN git config --global pull.rebase false

