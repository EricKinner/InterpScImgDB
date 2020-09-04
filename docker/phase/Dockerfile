FROM cupy/cupy:v6.5.0-python2

# Update system
RUN apt-get update

# Install os dependencies
RUN apt-get install -y tar python3 python3-pip python3-tk python2.7 python-pip python-tk python-qt4 python2.7-tk

# Install project dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pillow
RUN python2.7 -m pip install --upgrade pip enum34
RUN python2.7 -m pip install sewar==0.4.2 scipy numpy scikit-image pyPyrTools

# Copy and extract project
COPY Workspace.tar.gz /home/
RUN cd /home/ && tar xzf /home/Workspace.tar.gz && rm Workspace.tar.gz

# Install custom pyPyrTools library 
RUN rm -R /usr/local/lib/python2.7/dist-packages/pyPyrTools
RUN mv /home/Workspace/pyPyrTools/ /usr/local/lib/python2.7/dist-packages/
RUN rm /usr/local/lib/python2.7/dist-packages/pyPyrTools/wrapConv.so
RUN cp /usr/local/lib/python2.7/dist-packages/wrapConv.so /usr/local/lib/python2.7/dist-packages/pyPyrTools/

# Run consolidated script for interpolation and evaluation
ENTRYPOINT ["python2.7", "/home/Workspace/main.py"]

# Provide interactive shell
#CMD ["/bin/bash"]
