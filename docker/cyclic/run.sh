#!/bin/sh
sudo docker run --rm -it --gpus all -v "$1":/home/Workspace/data cyclic $2 $3 $4
sudo chown -R "$(whoami)":"$(whoami)" "$1"
