# This file is for use as a .vscode devcontainer
# The devcontainer should run as root and use user-mode podman or
# docker with user namespaces.
#
# This Dockerfile is built locally when creating a devcontainer,
# it is intended for individual developer customization

FROM ghcr.io/epics-containers/dev-u22-workspace

RUN pip install python3-pip-skeleton[dev] epics-containers-cli ibek

# create the cli-tools subcontainer launchers
ENV PATH=/cli-tools/tools:$PATH
RUN git clone https://github.com/epics-containers/cli-tools.git
