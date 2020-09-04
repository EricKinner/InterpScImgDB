#!/bin/sh
sudo docker image rm cyclic
sudo tar -czf Workspace.tar.gz ./Workspace/
sudo docker image build -t cyclic .
sudo rm Workspace.tar.gz
