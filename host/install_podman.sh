#!/bin/bash

this_dir=$(realpath $(dirname ${0}))

sudo apt install -y fuse 
wget http://ftp.us.debian.org/debian/pool/main/libp/libpod/podman_4.2.0+ds1-3_amd64.deb
sudo apt install -y podman_*
rm podman_*

cp ${this_dir}/storage.conf $HOME/.config/containers 

# publish a user socket for use as the remote podman from inside devcontainers
systemctl --user enable podman.socket
