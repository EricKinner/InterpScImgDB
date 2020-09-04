from PIL import Image, ImageChops
import numpy as np
import shutil
import sewar
import math
import sys
import os

from utils import *

def computeError(gt_path, test_path, diff_path, error_data):
	
	gt_fileList = os.listdir(gt_path)
	gt_fileList = sorted(gt_fileList)
	gt_fileListLen = len(gt_fileList)
	
	test_fileList = os.listdir(test_path)
	test_fileList = sorted(test_fileList)
	test_fileListLen = len(test_fileList)
	
	fileListLen = min(test_fileListLen, gt_fileListLen)

	if not os.path.exists(diff_path):
		os.makedirs(diff_path)
	
	for i in range(fileListLen):
		
		sys.stdout.write("\rProgress [" + str(int((float(i) / float(fileListLen)) * 100)) + "%]")
		
		gt_imgPath = os.path.join(gt_path, gt_fileList[i])
		img = Image.open(gt_imgPath)
		gt_img = img.copy()
		img.close()
		
		test_imgPath = os.path.join(test_path, test_fileList[i])
		img = Image.open(test_imgPath)
		test_img = img.copy()
		img.close()
	
		#---------------
	
		diffFileName = getFileNameWithoutExtension(gt_fileList[i]) + "_diff" + getFileExtension(gt_fileList[i])
		diffFileNamePath = os.path.join(diff_path, diffFileName)
		if(os.path.exists(diffFileNamePath)):
			continue
	
		diffImg = ImageChops.difference(gt_img, test_img)
		diffImg.save(diffFileNamePath)
		
		#---------------
		
		np_gt_img	= np.array(gt_img)
		np_test_img = np.array(test_img)
	
		# Skip error computation for identical images
		error_mse	= sewar.full_ref.mse(np_gt_img, np_test_img)
		if(error_mse == 0):
			continue
		
		error_ms_ssim 	= sewar.full_ref.msssim(np_gt_img, np_test_img).real
		error_psnr 		= 20 * math.log10(255) - 10 * math.log10(error_mse)
		error_ssim		= sewar.full_ref.ssim(np_gt_img, np_test_img)[0]
		error_vifp		= sewar.full_ref.vifp(np_gt_img, np_test_img)
		error_uqi		= sewar.full_ref.uqi(np_gt_img, np_test_img)
		
		error_data.append(i)
		error_data.append(error_mse)
		error_data.append(error_ssim)
		error_data.append(error_ms_ssim)
		error_data.append(error_psnr)
		error_data.append(error_vifp)
		error_data.append(error_uqi)
		
	sys.stdout.write("\r               \r")
		
	return error_data
