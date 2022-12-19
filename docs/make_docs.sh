#!/bin/bash

# a script to locally test documentation build.

sphinx-build -EWT --keep-going docs ${root}/build/html "${@}"