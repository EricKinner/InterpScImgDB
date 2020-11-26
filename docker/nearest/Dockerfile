FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y python3 python3-pip

# Install python dependencies
RUN pip3 install scikit-image sewar

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python3", "/home/Workspace/main.py"]

# Provide interactive shell
# CMD ["/bin/bash"]
