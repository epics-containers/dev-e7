# dls-python-workspace
DLS python workspace files

## How to adopt

Choose a workspace folder. This may have multiple python projects as subfolders or you can add them later.

```bash
cd <my_workspace_folder>
git clone git@github.com:epics-containers/vscode-python3-workspace.git
ln -s  vscode-python3-workspace/.devcontainer .
ln -s  vscode-python3-workspace/vscode-python3.code-workspace .
code vscode-python3.code-workspace
```

Click "Reopen in a Container" when prompted.

By default the workspace will contain a single folder ``.devcontainer``. If needed edit these files to alter the developer container and choose ``Rebuild Container``.

## Adopting updates

You are free to make changes to the workspace files. You can re-adopt updates with

```bash
cd <my_workspace_folder>/dls-python-workspace
git pull
```

If you want to version control your changes then use a fork of git@github.com:epics-containers/dls-python-workspace.git so you can push your individual changes back.
