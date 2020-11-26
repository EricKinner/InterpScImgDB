FROM cupy/cupy 

ARG DEBIAN_FRONTEND=noninteractive

# Update system
RUN apt-get update
RUN apt-get install -y python3-tk
RUN pip3 install pillow sewar matplotlib pyPyrTools scikit-image

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz

# Install custom pyPyrTools library 
RUN rm -R /usr/local/lib/python3.6/dist-packages/pyPyrTools
RUN mv /home/Workspace/pyPyrTools/ /usr/local/lib/python3.6/dist-packages/
RUN rm /usr/local/lib/python3.6/dist-packages/pyPyrTools/wrapConv.so
RUN cp /usr/local/lib/python3.6/dist-packages/wrapConv*.so /usr/local/lib/python3.6/dist-packages/pyPyrTools/wrapConv.so
 
# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python3", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
