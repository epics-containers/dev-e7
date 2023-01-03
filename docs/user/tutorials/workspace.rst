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
- File->Save Workspace As ...
- choose a filename for your workspace. IMPORTANT - save this in root_folder_for_your_new_workspace
  - the default folder will be .devcontainer and you don't want that.
- ctrl-shift-P Reopen in Container

At this point you have a workspace containing a single folder called .devcontainer.
This workspace is open in vscode and vscode is using the developer container
defined in .devcontainer. This devcontainer uses dev-e7 has the base container
plus customizations in .devcontainer/Dockerfile. You are free to customize
the developer container by editing files in .devcontainer.

Now add some projects to work on in this workspace as follows:

- open a terminal in vscode
- cd ..
- clone https://github.com/your_org/your_first_repo_for_this_workspace
- ctrl-shift-P add folder to Workspace ...
- choose the above repo folder

That's it you now have a devcontainer workspace.

Install your python projects into the global virtual environment
----------------------------------------------------------------

Once in you are inside the workspace container the ``pie`` script will
add an editable install of your python project into the the global virtual
environment /venv::

    pie *

Note that non-python project folders will be skipped see ``pie -h`` for details.
