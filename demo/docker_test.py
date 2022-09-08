"""
Example docker API client.

To try this, start the podman_service listening on docker API socket,
install python docker, run this script and then exec a shell in the
container it launches. i.e.:

podman_service
pip install docker
python demo/docker_test.py
podman exec -it python_docker sh

"""
from docker import from_env

docker_client = from_env()

container = docker_client.containers.run(
    "docker.io/alpine",
    detach=True,
    restart_policy={"Name": "unless-stopped"},
    # volumes={
    #     "/root/data": {"bind": "/data", "mode": "rw"},
    # },
    name="python_docker",
    command="sleep 10000",
)
