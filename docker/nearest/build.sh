#!/bin/sh
sudo docker image rm phase
sudo tar -czf Workspace.tar.gz ./Workspace/
sudo docker image build -t nearest .
sudo rm Workspace.tar.gz