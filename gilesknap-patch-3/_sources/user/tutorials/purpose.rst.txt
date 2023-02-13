Why to use dev-e7
------------------

dev-e7 and .devcontainer together provide a portable, customizable
development environment for any project.

Using a container for development means:

- you have freedom to add any system dependencies or change system
  configuration even if you don't have rights to do so on your host machine
- you can bring up your development environment quickly on any host
  that has a container runtime installed
- you can archive your environment along with your source so that you
  can reproduce it later
- collaboration with other developers no longer requires any lengthy
  setup
- etc (I think there is more to say here)

This devcontainer was created to be used in developing epics containers
generic IOCs and python3-pip-skeleton based python modules. However,
the customization options make it applicable to any software project that
builds on linux.