FROM cupy/cupy

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y libxml2 libglib2.0-0 libsm6 libxext6 libxrender-dev
RUN apt-get install -y python3 python3-pip  

# Install project dependencies
RUN pip3 install pillow requests numpy==1.17.3 torch==0.4.1 opencv-python==4.1.1.26 cffi easydict sewar

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz
RUN /home/Workspace/tools/downloadVoxelModel.py
# NOTE(eric): https://drive.google.com/uc?export=download&id=1FB-mpS4UokiLriDBNJSBmozMQRH0Qez1

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python3", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
