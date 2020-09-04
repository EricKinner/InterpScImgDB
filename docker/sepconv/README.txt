Docker Image for 
Video Frame Interpolation via Adaptive Separable Convolution (Niklaus et al. (2017) [1])
========================================================================================

Requirements:
-------------

	- Docker (Installation guide [3])
	- NVIDIA Docker (Installation guide [4])
	- gzip

Import Image:
-------------

-	gzip -d <<filename>>
	
		<<filename>> 	Name of compressed archive [sepconv.tar.gz]

-	sudo docker image load -i <<filename>>
	
		<<filename>>	Name of the image archive [sepconv.tar]

Example Usage: 
--------------

-	sudo docker run --rm -it --gpus all -v <<inputDir>>:/home/Workspace/data sepconv <<args>>
	
	<<inputDir>> 	Full path to directory containing all images
	
	<<args>>	--skip <<number>>		Optional argument. Skips <<number>> amount of images in the dataset, interpolates them, 
										and compares them to ground truth. Default is one. If zero is specified the images are 
										interpolated once and not compared.
											
											<<number>> should be one of [0, 1, 3, 7]

Notes:
------

Since docker is executed as root, the results will be owned by the linux user root. You might want to automate the invokation 
and change of ownership through a small shell script.

Examples:
---------

build.sh:

	#!/bin/sh
	sudo docker image rm sepconv
	sudo tar -czf Workspace.tar.gz ./Workspace/
	sudo docker image build -t sepconv .
	sudo rm Workspace.tar.gz
	
run.sh:

	#!/bin/sh
	sudo docker run --rm -it --gpus all -v "$1":/home/Workspace/data sepconv $2 $3 $4
	sudo chown -R "$(whoami)":"$(whoami)" "$1"

				
References:
-----------

[1] S. Niklaus, L. Mai, and F. Liu, “Video frame interpolation via adaptive separable convolution,” 
CoRR, vol. abs/1708.01692, 2017. [Online]. Available: http://arxiv.org/abs/1708.01692
	
[3] https://docs.docker.com/install/linux/docker-ce/debian/

[4] https://github.com/NVIDIA/nvidia-docker
