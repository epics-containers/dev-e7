Prepare your workstation
------------------------

TODO: tidy and flesh out.

The theory of devcontainers is that you don't need to set up your development
environment on your workstation. However, there are some things that you will
need to do once only to get started.

- Install podman 4.2 or higher OR install a recent version of Docker
- Install vscode 1.73 or newer
- Optionally install autossh, a socks proxy to communicate with your
  kubernetes cluster if it is not directly accessible from your workstation
  (e.g. working from home)
- make sure you have a kubectl configuration set up in $HOME/.kube/config
  that points to your kubernetes cluster

The following script can be used to launch a socks proxy once you
have installed autossh::

    #!/bin/bash
    if pgrep autossh; then
    echo "autossh is already running"
    else
    echo "Starting autossh"
    nohup autossh -N -D9090 -o ServerAliveInterval=10 auser@ssh.diamond.ac.uk > /tmp/autossh.log &
    fi

After installing podman make sure that the file
${HOME}/.config/containers/storage.conf specifies the overlay storage driver::

    [storage]
        driver = "overlay"
    [storage.options]
        mount_program = "/bin/fuse-overlayfs"

DLS users that want to connect to our pollux cluster can create a
.kube/config file that looks like this::

    ########################## EXAMPLE #############################################
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority: /home/USER/.kube/pollux_ca.crt
        server: https://api.pollux.diamond.ac.uk:6443
        proxy-url: socks5://localhost:9090
        name: pollux
    contexts:
    - context:
        cluster: pollux
        user: cluster-user
        namespace: bl45p
        name: cluster-user@pollux
    current-context: cluster-user@pollux
    kind: Config
    preferences: {}
    users:
    - name: cluster-user
        user:
        exec:
            apiVersion: client.authentication.k8s.io/v1beta1
            command: kubectl
            args:
            - oidc-login
            - get-token
            - --oidc-issuer-url=https://pollux-keycloak.diamond.ac.uk/auth/realms/diamond
            - --oidc-client-id=kubernetes
            - --oidc-client-secret=REDACTED
            - --grant-type=password
            - --token-cache-dir=/home/giles/.kube/cache/pollux/oidc-login

To make this work you would also need to copy from:

/dls_sw/apps/kubernetes/pollux/ca.crt

to:
pollux_ca.crt

(and replace 'USER' with your username above)
