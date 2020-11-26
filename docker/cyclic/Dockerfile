FROM tensorflow/tensorflow:latest-gpu

ARG DEBIAN_FRONTEND=noninteractive

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get install -y unzip python3 python3-pip

# Install project dependencies
RUN pip3 install pillow requests numpy==1.16.2 tensorflow-gpu==1.14.0 scipy==1.2.1 opencv-python==4.1.1.26 sewar

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz
RUN /home/Workspace/tools/downloadCyclicModel.py && cd /home/Workspace/install && unzip ckpt.zip && rm ckpt.zip
# NOTE(eric): https://drive.google.com/uc?export=download&confirm=X8zD&id=1X7PWDY2nAx8ZeSLso5qeypRUCDokNFms

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python3", "/home/Workspace/main.py"]

# Provide interactive shell
# CMD ["/bin/bash"]
