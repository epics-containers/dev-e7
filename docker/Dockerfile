
# This file is for use as a .vscode devcontainer
# The devcontainer should run as root and use user-mode podman or
# docker with user namespaces.

FROM ubuntu:22.04 as setup

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get upgrade -y && \
    apt-get install -yq --no-install-recommends \
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


########## add kubernetes cli tools ############################################

# kubectl
RUN curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list && \
    apt-get update && \
    apt-get install -y kubectl

# helm
RUN curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | tee /usr/share/keyrings/helm.gpg > /dev/null && \
    apt-get install apt-transport-https --yes && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | tee /etc/apt/sources.list.d/helm-stable-debian.list && \
    apt-get update && \
    apt-get install helm

# oidc-login
RUN curl -L https://github.com/int128/kubelogin/releases/download/v1.25.3/kubelogin_linux_amd64.zip --output /tmp/kubelogin.zip && \
    unzip /tmp/kubelogin.zip kubelogin && \
    mv kubelogin /usr/local/bin/kubectl-oidc_login


########## environment #########################################################

ENV DEV_PROMPT=E7

######### Stage to add a recent podman client ##################################

FROM setup as podman

# Compile podman https://techviewleo.com/how-to-install-podman-on-ubuntu/
# We install the podman to use its client CLI only. We require a recent
# version because it automatically uses remote when it sees CONTAINER_HOST in
# the environment. Also because we will need to keep within a few
# minor versions of the host podman for API compatibility

RUN apt-get install -yq golang-go btrfs-progs \
    libassuan-dev libbtrfs-dev libc6-dev libdevmapper-dev libglib2.0-dev \
    libgpgme-dev libgpg-error-dev libprotobuf-dev libprotobuf-c-dev  \
    libseccomp-dev libselinux1-dev libsystemd-dev

RUN wget https://github.com/containers/podman/archive/refs/tags/v4.3.1.tar.gz && \
    tar xvf v4.3.1.tar.gz && \
    cd podman*/ && \
    make BUILDTAGS="selinux seccomp" && \
    make install PREFIX=/podman

######### Stage to enable podman client inside the container ###################

FROM setup as devcontainer

# runtime dependencies of podman client
RUN apt-get install -yq libgpgme11 libdevmapper1.02.1

COPY --from=podman /podman /usr

# Point podman at the host ("outside") podman's user socket
# On the host this requires enabling a user podman service (once only):
#   systemctl enable --user podman.socket
#   systemctl start --user podman.socket
# Plus some podman arguments when launching, i.e.:
#   podman run -it -e CONTAINER_HOST=unix:/var/run/docker.sock -v=${XDG_RUNTIME_DIR}/podman/podman.sock:/var/run/docker.sock --security-opt=label=disable ghcr.io/epics-containers/dev-e7:latest
# This works for docker clients too, as the socket inside is the docker default.
ENV CONTAINER_HOST="unix:/var/run/docker.sock"

# let docker clients find a docker-like cli if they need it
RUN ln -s /usr/bin/podman /usr/bin/docker

######### Add in EPICS 7 tools and build environ ###############################

ENV EPICS_ROOT=/repos/epics
ENV EPICS_BASE=${EPICS_ROOT}/epics-base
ENV EPICS_HOST_ARCH=linux-x86_64
ENV PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

COPY --from=ghcr.io/epics-containers/epics-base-linux-developer:23.2.1 ${EPICS_BASE} ${EPICS_BASE}

######### Misc Tools ###########################################################

# add pie (python install editable) script in the path
COPY pie /usr/local/bin/pie

RUN git config --global pull.rebase false

