Docker Image for 
Phase-based frame interpolation for video (Meyer et al. (2015) [1])
===================================================================

Requirements:
-------------

	- Docker (Installation guide [2])
	- NVIDIA Docker (Installation guide [3])

Build image:
------------

sudo tar -czf Workspace.tar.gz ./Workspace/
sudo docker image build -t phase .
sudo rm Workspace.tar.gz

Run image:
----------

sudo docker run --rm -it --gpus all -v "$1":/home/Workspace/data phase ${@:2}
sudo chown -R "$(whoami)":"$(whoami)" "$1"

Arguments: 
----------

	./run.sh <<inputDir>> <<args...>>

	<<inputDir>> 	Full path to directory containing all images
	
	<<args>>	--skip <<number>>		Optional argument. Skips <<number>> amount of images in the dataset, interpolates them, 
											and compares them to ground truth. Default is zero. If zero is specified the images 
											are interpolated once and not compared.
											
											<<number>> should be [0, 1, 2, ..., 10]
																	
				--noErr					Skips the computation of the error metrics
				
				--noDiff				Skips the computation of the difference images 
				
References:
-----------

[1] S. Meyer, O. Wang, H. Zimmer, M. Grosse, and A. Sorkine-Hornung, “Phase-based frame interpolation for video,” 
in 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2015, pp. 1410–1418.
	
[2] https://docs.docker.com/install/linux/docker-ce/debian/

[3] https://github.com/NVIDIA/nvidia-docker
