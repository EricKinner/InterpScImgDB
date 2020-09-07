FROM pytorch/pytorch:1.0.1-cuda10.0-cudnn7-devel
#FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

ARG DEBIAN_FRONTEND=noninteractive

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y wget tar
RUN apt-get install -y python3 python3-pip python3-tk
RUN apt-get update
RUN apt-get install -y python2.7 python-pip python2.7-tk

#RUN echo "deb http://dk.archive.ubuntu.com/ubuntu/ xenial main" >> /etc/apt/sources.list
#RUN echo "deb http://dk.archive.ubuntu.com/ubuntu/ xenial universe" >> /etc/apt/sources.list
#RUN apt-get update
#RUN apt-get install -y gcc-4.9 g++-4.9
#RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 50
#RUN update-alternatives --install /usr/bin/g++ gcc /usr/bin/g++-4.9 50

# Install project dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pillow scipy==1.0.0
# torch=1.0.0
RUN python2.7 -m pip install --upgrade pip enum34
RUN python2.7 -m pip install sewar==0.4.2 pillow

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz

# Install project
RUN cd /home/Workspace/install/my_package && ./build.sh
RUN cd /home/Workspace/install/PWCNet/correlation_package_pytorch1_0 && ./build.sh
RUN cd /home/Workspace/install/model_weights && wget http://vllab1.ucmerced.edu/~wenbobao/DAIN/best.pth

RUN python3 -m pip install scipy==1.0.0 pillow

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python2.7", "/home/Workspace/main.py"]

# Provide interactive shell
# CMD ["/bin/bash"]
