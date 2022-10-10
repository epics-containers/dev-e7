#!/bin/bash
if pgrep autossh; then
  echo "autossh is already running"
else
  echo "Starting autossh"
  nohup autossh -N -D9090 -o ServerAliveInterval=10 auser@ssh.diamond.ac.uk > /tmp/autossh.log &
fi
