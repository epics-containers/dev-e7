"""
Example docker API client.

To try this, start the podman_service listening on docker API socket,
install python docker, run this script and then exec a shell in the
container it launches. i.e.:

podman_service
pip install docker
python demo/docker_test.py
podman exec -it python_docker sh
exit
podman rm -f python_docker

NOTE: warnings about cgroups are expected and I believe this is due to RHEL8
not having the full cgroupV2 support? (I don't get this on Ubuntu 22.04)

"""
from docker import from_env

docker_client = from_env()

container = docker_client.containers.run(
    "docker.io/alpine",
    detach=True,
    restart_policy={"Name": "unless-stopped"},
    volumes={"/home": {"bind": "/home2", "mode": "rw"}},
    name="python_docker",
    command="sleep 10000",
)
