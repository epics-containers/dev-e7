#!/bin/bash

# a script to locally test documentation build.

root=$(realpath $(dirname ${BASH_SOURCE[0]})/..)

sphinx-build -EWT --keep-going docs ${root}/build/html "${@}"