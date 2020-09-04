Docker Image for 
Nearest Neighbor "Interpolation"
================================

Requirements:
-------------

	- Docker (Installation guide [1])
	- NVIDIA Docker (Installation guide [2])
	- gzip

Import Image:
-------------

-	gzip -d <<filename>>
	
		<<filename>> 	Name of compressed archive [nearest.tar.gz]

-	sudo docker image load -i <<filename>>
	
		<<filename>>	Name of the image archive [nearest.tar]

Example Usage: 
--------------

-	sudo docker run --rm -it --gpus all -v <<inputDir>>:/home/Workspace/data nearest <<args>>
	
	<<inputDir>> 	Full path to directory containing all images
	
	<<args>>	--skip <<number>>		Optional argument. Skips <<number>> amount of images in the dataset, interpolates them, 
											and compares them to ground truth. Default is zero. If zero is specified the images 
											are interpolated once and not compared.
											
											<<number>> should be [0, 1, 2, ..., 10]

Notes:
------

Since docker is executed as root, the results will be owned by the linux user root. You might want to automate the invokation and change of ownership
through a small shell script.

In order to be able to run the script on a laptop, I downscaled the input images. For large cluster applications, this probably can be removed again
to produce better quality.

Examples:
---------

build.sh:

	#!/bin/sh
	sudo docker image rm nearest
	sudo tar -czf Workspace.tar.gz ./Workspace/
	sudo docker image build -t nearest .
	sudo rm Workspace.tar.gz
	
run.sh:

	#!/bin/sh
	sudo docker run --rm -it --gpus all -v "$1":/home/Workspace/data nearest $2 $3 $4
	sudo chown -R "$(whoami)":"$(whoami)" "$1"
				
References:
-----------
	
[1] https://docs.docker.com/install/linux/docker-ce/debian/

[2] https://github.com/NVIDIA/nvidia-docker
