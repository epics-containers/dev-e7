Host Setup
==========

## Intro

This folder contains a few tips on setting up the host in which you run the
dev-u22 workspace devcontainer.

The container is intended to be portable between hosts but a little setup is
required as follows.

You will need:

- vscode installed from https://code.visualstudio.com/download
- preferably podman as the container manager (see below)
  - docker or WSL2 also will work
- kube config file for connecting to your cluster
- a .bashrc_dev file in your home directory to configure dev-u22 containers

Optional additions:

- a socks proxy to communicate with the cluster if it is not accessible directly
  from your host

## install podman

If you already have docker installed then this is an option. Most testing has
been done with podman so this is recommended.

To install the latest podman on a debian host, run the script install_podman.sh.

If you already have an old installation of podman then perform these steps
first:
    podman system reset
    apt remove podman

Note that the script does:
    systemctl --user enable podman.socket

Which runs a user mode podman exposing a socket for use from inside 
devcontainers

TODO: how to install on other systems

## .bashrc_dev

Copy the .bashrc_dev from this folder to your home directory and edit
to match your configuration

## kube configuration

An example kube configuration config_pollux is included for reference. You
will need to get the equivalent from your cluster admin.

## socks proxy

At the top of the example kube configuration is ``proxy-url`` this allows
you to use a socks proxy into your organization's network, assuming you have
an external ssh login capability. 

You will require a local autossh forwarder running locally for this to work
The script ``socks.sh`` will set this up for you.

## VPN 

As an alternative to using socks you can use a VPN.

If you have a VPN to your organization network then you can enable that 
and remove ``proxy-url`` from .kube config.

