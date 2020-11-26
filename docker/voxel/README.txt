Docker Image for 
Video Frame Synthesis using Deep Voxel Flow (Liu et al. (2017) [1])
===================================================================

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

[1] X. T. Y. L. Ziwei Liu, Raymond Yeh and A. Agarwala, “Video frame synthesis using deep voxel flow,” 
in Proceedings of International Conference on Computer Vision (ICCV), October 2017.

[2] https://docs.docker.com/install/linux/docker-ce/debian/

[3] https://github.com/NVIDIA/nvidia-docker
