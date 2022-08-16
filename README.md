# dls-python-workspace
DLS python workspace files

## How to adopt

Choose a workspace folder. This may have multiple python projects as subfolders or you can add them later.

```bash
cd <my_workspace_folder>
git clone git@github.com:epics-containers/dls-python-workspace.git
ln -s  dls-python-workspace/.devcontainer .
ln -s  dls-python-workspace/dls-python-workspace.code-workspace .
code dls-python-workspace.code-workspace
```

Click "Reopen in a Container" when prompted.

## Adopting updates

You are free to make changes to the workspace files. You can re-adopt updates with

```bash
cd <my_workspace_folder>/dls-python-workspace
git pull
```

If you want to version control your changes then use a fork of git@github.com:epics-containers/dls-python-workspace.git so you can push your indevidual changes back.
