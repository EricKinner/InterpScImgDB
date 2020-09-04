FROM cupy/cupy

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y wget tar python3 python3-pip python3-tk python2.7 python-pip python2.7-tk

# Install project dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pillow torch
RUN python2.7 -m pip install --upgrade pip enum34
RUN python2.7 -m pip install sewar==0.4.2 pillow

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz
RUN cd /home/Workspace/install && wget --timestamping http://content.sniklaus.com/sepconv/network-lf.pytorch

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python2.7", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
