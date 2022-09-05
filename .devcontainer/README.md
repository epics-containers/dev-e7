Docker in Podman plus Podman outside Podman
===========================================

This branch docker-in-docker adds the ability to run docker containers 
inside the dev container but also control the host podman from inside the
container (using the docker cli connected to a user podman socket)

HOWEVER: I'm having issues making this work on RHEL8 and am parking it 
until RHEL9. It does work when the host is Ubuntu 22.04.


