Docker Image for 
Depth-Aware Video Frame Interpolation (Bao et al. (2019) [1])
===================================================================

Requirements:
-------------

	- Docker (Installation guide [3])
	- NVIDIA Docker (Installation guide [4])
	- gzip

Import Image:
-------------

-	gzip -d <<filename>>
	
		<<filename>> 	Name of compressed archive [dain.tar.gz]

-	sudo docker image load -i <<filename>>
	
		<<filename>>	Name of the image archive [dain.tar]

Example Usage: 
--------------

-	sudo docker run --rm -it --gpus all -v <<inputDir>>:/home/Workspace/data dain <<args>>
	
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
	sudo docker image rm dain
	sudo tar -czf Workspace.tar.gz ./Workspace/
	sudo docker image build -t dain .
	sudo rm Workspace.tar.gz
	
run.sh:

	#!/bin/sh
	sudo docker run --rm -it --gpus all -v "$1":/home/Workspace/data dain $2 $3 $4
	sudo chown -R "$(whoami)":"$(whoami)" "$1"
				
References:
-----------

[1] Bao, Wenbo and Lai, Wei-Sheng and Ma, Chao and Zhang, Xiaoyun and Gao, Zhiyong and Yang, Ming-Hsuan, “Depth-Aware Video Frame Interpolation” 
in 2019 IEEE Conference on Computer Vision and Pattern Recognition
	
[3] https://docs.docker.com/install/linux/docker-ce/debian/

[4] https://github.com/NVIDIA/nvidia-docker
