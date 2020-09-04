#!/bin/sh
sudo docker image rm sepconv
sudo tar -czf Workspace.tar.gz ./Workspace/
sudo docker image build -t sepconv .
sudo rm Workspace.tar.gz
