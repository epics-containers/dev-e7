# dev-u22-workspace

This template project implements a devcontainer for use as a workspace
for multiple projects.

It also includes VSCode workspace settings files and a vscode devcontainer
definition file. The default workspace settings will work well with python
projects that use https://github.com/DiamondLightSource/python3-pip-skeleton,
but other python projects and other languages will also work.

Use cases:

- Allows for personalized container environment / VSCode settings that
  don't contaminate the individual projects.
- Provides a devcontainer that can manage more than one project in
  a workspace (skeleton based projects or otherwise)
- Provides a devcontainer wrapper for projects that do not have their own
  devcontainer. Useful for collaboration projects where upstream is not
  adopting devcontainers or skeleton.
- Provides VSCode settings at the level of the Workspace

# Prerequisites

The host folder in this project provides information on setting up a 
workstation to run this devcontainer. See [host](host/README.md)
# Features

## Containers in Containers
Docker and Podman CLI and API are supported inside the container. They all
connect to the user podman instance running on the host.

## Kubernetes CLI tools
Inlcudes kubectl, helm and oidc-login. Set environment ``KUBECONFIG`` to 
point to your kubectl configuration file in order for these tools to 
pick up cluster configuration.

DLS users need to either:

- run ``module load pollux`` before launching the devcontainer.
- add this to $HOME//bashrc_dev  
  - export KUBECONFIG=$HOME/.kube/config_pollux

Uses the home directory .kube user folder for cluster configuration.

## Global VirtualEnv
- The virtualenv /venv is already in the path and pre-populated with the
  skeleton dev dependencies.
- You are free to create additional venvs inside the container if the projects
  inside have conflicting dependencies, but this should not usually be needed.

## .bashrc_dev
- This file is mounted as /root/.bashrc and provides a starting point for
  your bash profile inside the container. Includes:
  - autocompletion for git and bash
  - shared bash history with the host
  - will also execute a personal run commands file if found at
    - $HOME/.bashrc_dev

# How to adopt
- Take a copy of the template project
  - go to https://github.com/epics-containers/dev-u22-workspace
  - click "Use this template"
  - choose a name and organization for your workspace project
- Clone the new repo as a peer to the project or projects that it will manage
- cd into the project folder and launch vscode
  - code dev-u22.code-workspace
- Click "Reopen in a Container" when prompted
- "File -> Add Folder to Workspace" for as many peer projects as you wish
- choose ``Python: Select interpreter`` command (access via ctrl-shift-P)
  choose ``select at workspace level`` and select /venv/bin/python.

# Adopting updates

Changes you make can be committed back to your own repo. You can re-adopt
updates to the original template with the following commands.
Merge conflicts will need to be resolved where you have changed files.

```bash
cd <workspace repo folder>
# first update
git pull git@github.com:epics-containers/dev-u22-workspace.git --allow-unrelated-histories
# subsequent updates
git pull git@github.com:epics-containers/dev-u22-workspace.git
```

# Tips and Tricks

## open in default browser

When reviewing your documentation build you will need to open an html file
in a browser. Rather than installing a browser inside the devcontainer you 
can use the [provided vscode plugin](https://marketplace.visualstudio.com/items?itemName=peakchen90.open-html-in-browser).

Simply right-click on the html file in the explorer and choose
"Open in default browser"
