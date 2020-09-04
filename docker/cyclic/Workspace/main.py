import argparse
import shutil
import sys
import os

from interface import *
from error import *
from utils import *

parser = argparse.ArgumentParser(description='Main Interface')
parser.add_argument('--skip', help='number of images skipped', default=1, required=False)
args = parser.parse_args()

DATA_ROOT_PATH 		= "/home/Workspace/data/"
META_DATA_FILENAME 	= "cyclic_meta.csv"
ERROR_FILENAME 		= "cyclic_error.csv"
INSTALL_PATH 		= "/home/Workspace/install"
SKIP_NUM			= 1

def skipFrames(path, skipNum):
	
	fileList = os.listdir(path)
	imgList = filterImages(fileList)
	imgList = sorted(imgList)

	keepNum = skipNum + 1

	for counter, fileName in enumerate(imgList):
		
		if((counter % keepNum) != 0):
			os.remove(os.path.join(path, fileName))

def parseArgs():
	
	global SKIP_NUM
	SKIP_NUM = int(args.skip)
	
	if(SKIP_NUM != 0 and SKIP_NUM != 1 and SKIP_NUM != 3 and SKIP_NUM != 7):
		print("Invalid number of images to be skipped (" + str(SKIP_NUM) + ")")
		sys.exit(1)
		

if __name__ == "__main__":
	
	parseArgs()
	
	# Assume all images are in root directory
	
	origPath 	= os.path.join(DATA_ROOT_PATH, "orig")
	tempPath 	= os.path.join(DATA_ROOT_PATH, "temp")
	outPath 	= os.path.join(DATA_ROOT_PATH, "out")
	diffPath 	= os.path.join(DATA_ROOT_PATH, "diff")
	
	# Reset directory if anything was done
	
	if(os.path.exists(os.path.join(DATA_ROOT_PATH, META_DATA_FILENAME))):
		os.remove(os.path.join(DATA_ROOT_PATH, META_DATA_FILENAME))
		
	if(os.path.exists(os.path.join(DATA_ROOT_PATH, ERROR_FILENAME))):
		os.remove(os.path.join(DATA_ROOT_PATH, ERROR_FILENAME))
	
	if(os.path.exists(origPath)):
		moveAllFiles(origPath, DATA_ROOT_PATH)
		shutil.rmtree(origPath)
	
	if(os.path.exists(tempPath)):
		shutil.rmtree(tempPath)
		
	if(os.path.exists(outPath)):
		shutil.rmtree(outPath)
		
	if(os.path.exists(diffPath)):
		shutil.rmtree(diffPath)
	
	# Create directory structure
	
	os.makedirs(origPath)
	os.makedirs(tempPath)
	os.makedirs(outPath)
	
	moveAllFiles(DATA_ROOT_PATH, origPath)
	copyAllFiles(origPath, tempPath)
	skipFrames(tempPath, SKIP_NUM)
	
	# Do the interpolation
	
	print("Interpolating images ...")
	
	meta_data = []
	
	if(SKIP_NUM == 0 or SKIP_NUM == 1):
		meta_data = interpolate(tempPath, outPath, meta_data, INSTALL_PATH)
	elif(SKIP_NUM == 3):
		meta_data = interpolate(tempPath, outPath, meta_data, INSTALL_PATH)
		deleteAllFiles(tempPath)
		moveAllFiles(outPath, tempPath)
		meta_data = interpolate(tempPath, outPath, meta_data, INSTALL_PATH)
	elif(SKIP_NUM == 7):
		meta_data = interpolate(tempPath, outPath, meta_data, INSTALL_PATH)
		deleteAllFiles(tempPath)
		moveAllFiles(outPath, tempPath)
		meta_data = interpolate(tempPath, outPath, meta_data, INSTALL_PATH)
		deleteAllFiles(tempPath)
		moveAllFiles(outPath, tempPath)
		meta_data = interpolate(tempPath, outPath, meta_data, INSTALL_PATH)
	
	shutil.rmtree(tempPath)
	
	# Write out metadata
	
	meta_data_file = open(os.path.join(DATA_ROOT_PATH, META_DATA_FILENAME), "w")
	meta_data_file.write("Avg time per img, Total time, width, height, interp img num\n")
	meta_data_file.write(str(meta_data[0]) + "," + str(meta_data[1]) + "," + str(meta_data[2]) + "," + str(meta_data[3]) + "," + str(meta_data[4]) + "\n")
	meta_data_file.close()
	
	# Compute Error
	
	if(SKIP_NUM != 0):
			
		print("Calculating Errors ...")
		
		os.makedirs(diffPath)
		error_data = []
		error_data = computeError(origPath, outPath, diffPath, error_data)
	
		error_data_file = open(os.path.join(DATA_ROOT_PATH, ERROR_FILENAME), "w")
		error_data_file.write("Index, MSE, SSIM, MS_SSIM, PSNR, VIFP, UQI\n")
		
		counter = 0
		while(counter < len(error_data)):
			error_data_file.write(str(error_data[counter+0]) + "," + str(error_data[counter+1]) + "," + str(error_data[counter+2]) + "," + str(error_data[counter+3]) + "," + str(error_data[counter+4]) + "," + str(error_data[counter+5]) + "," + str(error_data[counter+6]) + "\n")
			
			counter = counter + 7;
		
		error_data_file.close()
		
	print("Done.")
	

