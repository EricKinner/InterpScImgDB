#!/bin/sh
sudo tar -czf Workspace.tar.gz ./Workspace/
sudo docker image build -t dain .
sudo rm Workspace.tar.gz
