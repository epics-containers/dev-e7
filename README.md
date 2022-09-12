# vscode-python3-workspace
VSCode workspace settings files for python projects including a 
developer container.


# Purpose of this project

Provides a vscode devcontainer environment for python projects. May be used
with the python skeleton project here:
https://github.com/DiamondLightSource/python3-pip-skeleton

Use cases:

- To provide a devcontainer that can manage more than one python project in
  a workspace (skeleton based projects or otherwise)
- To provide a devcontainer wrapper for projects that do not have their own
  devcontainer. Useful for collaboration projects where upstream is not
  adopting devcontainers or skeleton.

# Features
## Containers in Containers
- For details go see [podman inside](docs/podmaninside.md)

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
  - bash prompt with info including git branch
  
# How to adopt

- Take a copy of the template project 
  - go to https://github.com/epics-containers/vscode-python3-workspace
  - click "Use this template"
  - choose a name and organization for your workspace project
- Clone the new repo as a peer to the project or projects that it will manage
- cd into the project folder and launch vscode
  - code vscode-python3.code-workspace
- Click "Reopen in a Container" when prompted
- Add as many peer projects as you wish to the workspace
- choose ``Python: Select interpreter`` command (access via ctrl-shift-P) 
  choose ``select at workspace level`` and select /venv/bin/python.

# Adopting updates

Changes you make can be committed back to your own repo. You can re-adopt
updates to the original template with the following commands. 
Merge conflicts will need to be resolved where you have changed files.

```bash
cd <workspace repo folder>
# first update
git pull git@github.com:epics-containers/vscode-python3-workspace.git --allow-unrelated-histories
# subsequent updates
git pull git@github.com:epics-containers/vscode-python3-workspace.git
```
