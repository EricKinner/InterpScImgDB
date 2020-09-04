FROM cupy/cupy

# Update system
RUN apt-get clean
RUN apt-get update

# Install os dependencies
RUN apt-get install -y libxml2 tar  libglib2.0-0  libsm6 libxext6 libxrender-dev python3 python3-pip python3-tk python2.7 python-pip python2.7-tk

# Install project dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pillow requests numpy==1.17.3 torch==0.4.1 opencv-python==4.1.1.26 cffi easydict
RUN python2.7 -m pip install --upgrade pip enum34
RUN python2.7 -m pip install sewar==0.4.2

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz
RUN /home/Workspace/tools/downloadVoxelModel.py

# https://drive.google.com/uc?export=download&id=1FB-mpS4UokiLriDBNJSBmozMQRH0Qez1

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python2.7", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
