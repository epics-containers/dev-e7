Local Build and Test
====================

Clone the repository
--------------------

First clone the repository locally using `Git
<https://git-scm.com/downloads>`_::

    git clone git://github.com/epics-containers/dev-e7.git

Build the container
-------------------
The following command will build the container locally::

    podman build -t dev-e7 docker

If you have docker instead of podman just change podman to docker in the
above command.

This builds the container using the Dockerfile in the docker directory and
creates an image named dev-e7.

Run the container
-----------------

There is a launch script to launch the container (tagged with dev-e7) outside
of VSCode. This allows you to test the container without using the
VSCode devcontainers::

    ./launch_dev_podman

or if you have docker instead of podman::

    ./launch_dev_docker
