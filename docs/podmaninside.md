# UPDATE

I have switched to podman/docker outside only after experiencing performance
issues with "inside". This makes for much simpler Dockerfile and much less 
developer confusion! It means that all containers run in the host and share 
the same cache - so you only need to manage one cache.

To do docker/podman outside we simply:
- install podman 4.2
- set CONTAINER_HOST=unix:/var/run/docker.sock
- start a user socket on the host with 'systemctl --user start podman.socket
- map the socket:
  - podman -v=${XDG_RUNTIME_DIR}/podman/podman.sock:/var/run/docker.sock ...

# DEPRECATED
# Containers inside and outside of Containers

The provided devcontainer is intended to run in rootless podman.
It provides the following container in container features:

- rootful podman inside of the container
- rootful docker API inside of the container (provided by podman)
- access to the host podman outside of the container from inside

# Rootful podman inside the container

Podman is installed inside the container. Rootful in-container access
is the default when using the podman CLI.

e.g.

```
podman ps
```

# User podman outside of the container

To access the user's host podman just add -r to the podman command.
You can even use this to stop the container from inside of itself.

e.g.

```
podman -r ps
```

# Rootful Docker inside the container

This requires that you start a podman service listening on the default 
docker socket. The script /usr/bin/podman_service does this and is invoked
from the command line as follows.

```
podman_service
```

Any scripts that use ``docker`` cli will work as this is aliased to ``podman``
(and is mostly interchangeable). Any docker client code that accesses the 
API via the socket will also work since the podman service has docker API
compatibility.

For an example of using the docker API from python see the
[demo in this repo](../demo/docker_test.py).

