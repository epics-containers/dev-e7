Creating a Devcontainer Workspace
=================================

TODO tidy and flesh out.

Create a workspace
------------------

Most likely you want to fork this repo to create your personal developer container.

These steps clone directly from this repo, but you get the idea!

Create your vscode workspace as follow:

- cd root_folder_for_your_new_workspace
- git clone https://github.com/epics-containers/.devcontainer
- code .devcontainer
- open a terminal in vscode
- cd ..
- clone https://github.com/your_org/your_first_repo_for_this_workspace
- ctrl-shift-P add folder to Workspace ...
- choose the above repo folder
- File->Save Workspace As ...
- choose a filename for your workspace. IMPORTANT - save this in root_folder_for_your_new_workspace
  - the default folder will be .devcontainer and you don't want that.
- ctrl-shift-P Reopen in Container

That's it you now have a devcontainer workspace.

Install your python projects into the workspace
-----------------------------------------------

Once in you are inside the workspace container the following steps will
add an editable install of your python project into the the global virtual
environment /venv::

    cd /workspace_root_folder
    .devcontainer/pie *

Note that non-python project folders will be skipped.

Customization at container launch time
--------------------------------------

If you wish to install additional python packages or do any other setup
at container creation time then make changes to the this file:

.devcontainer/postCreateCommand.sh

Changes in this file will get executed at the start of each new
container instance but do not require rebuilding the container image.

Note that this file is in .gitignore because you may have multiple
workspaces with different python projects. You can use this file
to make changes on a per workspace basis without dirtying your
.devcontainer repo.

Customization at container build time
-------------------------------------

When vscode launches the container it does a build using the this Dockerfile]

.devcontainer/Dockerfile

Add or remove installation steps as needed.
