# This file is for use as a .vscode devcontainer
# The devcontainer should run as root and use user-mode podman or
# docker with user namespaces.

FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    apt-transport-https \
    autossh \
    build-essential \
    busybox \
    ca-certificates \
    curl \
    git \
    graphviz \
    net-tools \
    openssh-client \
    python3-dev \
    python3-pyqt5 \
    python3-venv \
    vim \
    x11-apps \
    && busybox --install


########## add podman and docker "outside" #####################################

# podman 4.2 has much better remote support than Ubuntu's apt repos version
RUN wget http://ftp.us.debian.org/debian/pool/main/libp/libpod/podman_4.2.0+ds1-3_amd64.deb && \
    apt install -y ./podman* && \
    rm podman*

# Point podman at the host ("outside") podman's user socket
# This requires starting a user podman service plus some podman arguments i.e.:
#   systemctl start podman.socket
#   podman run -it -e CONTAINER_HOST=unix:/var/run/docker.sock  \
#         -v=${XDG_RUNTIME_DIR}/podman/podman.sock:/var/run/docker.sock  \
#         --security-opt=label=type:container_runtime_t dev_ws:latest
# Works for docker clients too, as the socket inside is the default docker one.
ENV CONTAINER_HOST="unix:/var/run/docker.sock"

# let docker clients find a docker-like cli if they need it
RUN ln -s /usr/bin/podman /usr/bin/docker

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


########## add python virtual environment ######################################

ENV VIRTUALENV=/venv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH=${VIRTUALENV}/bin:/cli-tools/tools:$PATH
ENV DEV_PROMPT=U22

# install developer packages and tools
RUN pip install python3-pip-skeleton[dev] epics-containers-cli ibek
