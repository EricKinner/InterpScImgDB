#!/bin/bash
sudo docker run --rm -it --gpus all -v "$1":/home/Workspace/data nearest ${@:2}
sudo chown -R "$(whoami)":"$(whoami)" "$1"
