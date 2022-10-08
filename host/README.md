Host Setup
==========

The dev-u22 container is portable. Podman is preferred on the host in which 
the container will run, docker is not yet tested but should also work.

To install the latest podman on a debian host, run the script install_podman.sh.

If you already have an old installation of podman then perform these steps
first:

    podman system reset
    apt remove podman
