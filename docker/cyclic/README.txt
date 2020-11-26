Docker Image for 
Deep Video Frame Interpolation using Cyclic Frame Generation (Liu et al. (2019) [1])
====================================================================================

Requirements:
-------------

	- Docker (Installation guide [2])
	- NVIDIA Docker (Installation guide [3])

Build image:
------------

sudo tar -czf Workspace.tar.gz ./Workspace/
sudo docker image build -t cyclic .
sudo rm Workspace.tar.gz

Run image:
----------

sudo docker run --rm -it --gpus all -v "$1":/home/Workspace/data cyclic ${@:2}
sudo chown -R "$(whoami)":"$(whoami)" "$1"

Arguments: 
----------

	./run.sh <<inputDir>> <<args...>>

	<<inputDir>> 	Full path to directory containing all images
	
	<<args>>	--skip <<number>>		Optional argument. Skips <<number>> amount of images in the dataset, interpolates them, 
										and compares them to ground truth. Default is one. If zero is specified the images 
										are interpolated once and not compared.
											
										<<number>> should be one of [0, 1, 3, 7]
										
				--noErr					Skips the computation of the error metrics
				
				--noDiff				Skips the computation of the difference images 

References:
-----------

[1] Y.-L. Liu, Y.-T. Liao, Y.-Y. Lin, and Y.-Y. Chuang, “Deep video frame interpolation using cyclic frame generation,” 
in Proceedings of the 33rd Conference on Artificial Intelligence (AAAI), 2019.

[2] https://docs.docker.com/install/linux/docker-ce/debian/

[3] https://github.com/NVIDIA/nvidia-docker
