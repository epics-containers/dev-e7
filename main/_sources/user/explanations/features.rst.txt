Features of dev-u22
===================


Containers in Containers
------------------------
Docker and Podman CLI and APIs are supported inside the container. They all
connect to the user podman instance running on the host.

Kubernetes CLI tools
--------------------
Includes kubectl, helm and oidc-login. Set environment ``KUBECONFIG`` to
point to your kubectl configuration file in order for these tools to
pick up cluster configuration.

DLS users need to either:

- run ``module load pollux`` before launching the devcontainer.
- add this to $HOME/.bashrc_dev
  - export KUBECONFIG=$HOME/.kube/config_pollux

DLS kubectl users will also need to mount these folders into the container.

- /dls_sw/apps/kubernetes/pollux/
- /dls_sw/apps/kubernetes/argus/

OR copy the crt files into their %{HOME}/.kube folder. See `prepare`.

In the .devcontainer project these are commented out in the file
https://github.com/epics-containers/.devcontainer/blob/main/devcontainer.json

Uses the home directory .kube user folder for cluster configuration.

Global VirtualEnv
-----------------
This is a feature of .devcontainer project see
https://github.com/epics-containers/.devcontainer/blob/main/Dockerfile

- The virtualenv /venv is already in the path and pre-populated with the
  skeleton dev dependencies.
- You are free to create additional venvs inside the container if the projects
  inside have conflicting dependencies, but this should not usually be needed.

.bashrc_dev
-----------
This file is mounted as /root/.bashrc and provides a starting point for
your bash profile inside the container. Includes:

  - autocompletion for git and bash
  - shared bash history with the host
  - configuration for kubernetes
  - a shell prompt that tells you:

    - which container you are in
    - which git branch you are on
    - TODO: which kubernetes cluster you are connected to
