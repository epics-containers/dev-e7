Personalizing the Devcontainer
==============================

The files in .devcontainer define the development environment you will
use. You will have a clone of this repo in each workspace you create.
You may choose to have the same settings in all your workspaces or
have a number of forks of .devcontainer with different settings.

The key customization options are described below.

Customization at container launch time
--------------------------------------

If you wish to install additional python packages or do any other setup
at container creation time then make changes to the this file:

.devcontainer/postCreateCommand.sh

Changes in this file will get executed at the start of each new
container instance, you will need to rebuild the container for
changes to take affect.


Customization at container build time
-------------------------------------

When vscode launches the container it does a build using the this Dockerfile]

.devcontainer/Dockerfile

Add or remove installation steps as needed.
