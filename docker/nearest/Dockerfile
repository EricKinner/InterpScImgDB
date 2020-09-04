FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y tar python2.7 python-pip python-tk python-qt4 python2.7-tk

# Install project dependencies
RUN python2.7 -m pip install --upgrade pip enum34
RUN python2.7 -m pip install sewar==0.4.2 scipy numpy scikit-image

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python2.7", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
