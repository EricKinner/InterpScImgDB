FROM cupy/cupy

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y wget python3 python3-pip 

# Install python dependencies
RUN pip3 install pillow torch sewar

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz
RUN cd /home/Workspace/install && wget --timestamping http://content.sniklaus.com/sepconv/network-lf.pytorch

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python3", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
