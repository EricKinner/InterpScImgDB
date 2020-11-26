FROM pytorch/pytorch:1.0.1-cuda10.0-cudnn7-devel

ARG DEBIAN_FRONTEND=noninteractive

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y wget python3

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install pillow scipy==1.0.0 sewar

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz

# Install project
RUN cd /home/Workspace/install/my_package && ./build.sh
RUN cd /home/Workspace/install/PWCNet/correlation_package_pytorch1_0 && ./build.sh
RUN mkdir /home/Workspace/install/model_weights && cd /home/Workspace/install/model_weights && wget http://vllab1.ucmerced.edu/~wenbobao/DAIN/best.pth

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python3", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
