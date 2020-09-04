from PIL import ImageTk,Image
import shutil
import time
import sys 
import os

from utils import *

def numToStr4Digits(number):
	
	if(counter < 10):
		return "000" + str(counter)
	
	if(counter < 100):
		return "00" + str(counter)

	if(counter < 1000):
		return "0" + str(counter)

	return str(counter)

def runInterpolation(install_path, imgPath1, imgPath2, outPath):
	
	executable 	= "python3 /home/Workspace/install/train.py"
	command 	=  executable + " '" + imgPath1 + "' '" + imgPath2 + "' '" + outPath + "'"
	os.system(command)

def interpolate(input_path, output_path, meta_data, install_path):
	
	fileList = os.listdir(input_path)
	
	imgList = filterImages(fileList)
	imgList = sorted(imgList)
	
	#-------------------------------
	
	totalNum 	= len(imgList)
	lastFrame 	= None
	totalTime 	= 0
	
	for counter, imgName in enumerate(imgList):
		
		sys.stdout.write("\rProgress [" + str(int((float(counter) / float(totalNum)) * 100)) + "%]")
		
		out_imgName = getFileNameWithoutExtension(imgName) + "-00" + getFileExtension(imgName)
		shutil.copyfile(os.path.join(input_path, imgName), os.path.join(output_path, out_imgName))
		
		if(lastFrame == None):
			lastFrame = imgName
			continue
			
		out_imgName = getFileNameWithoutExtension(lastFrame) + "-50" + getFileExtension(lastFrame)
		out_imgPath = os.path.join(output_path, out_imgName)
	
		if(os.path.exists(out_imgPath)):
			continue
	
		start = time.time()
		
		runInterpolation(install_path, os.path.join(input_path, lastFrame), os.path.join(input_path, imgName), out_imgPath)
		
		end = time.time()
		totalTime += end - start
			
		lastFrame = imgName
	
	sys.stdout.write("\r               \r")
	
	#-------------------------------
	
	resolution = Image.open(os.path.join(input_path, imgList[0])).size
	
	interpImgNum 	= totalNum - 1
	avgTime 		= totalTime / interpImgNum
	
	if(len(meta_data) == 0):
		meta_data.append(avgTime)
		meta_data.append(totalTime)
		meta_data.append(resolution[0])
		meta_data.append(resolution[1])
		meta_data.append(interpImgNum)
	else:
		meta_data[1] = meta_data[1] + totalTime
		meta_data[4] = meta_data[4] + interpImgNum
		meta_data[0] = meta_data[1] / meta_data[4]
	
	return meta_data
	
