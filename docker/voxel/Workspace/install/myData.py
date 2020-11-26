import os
import numpy as np
import cv2
import torch
from PIL import Image
from torch.utils.data import Dataset
from core.utils import transforms as tf
from shutil import copyfile

class MyData(Dataset):

	def __init__(self, imgPath_0, imgPath_1):
		super()
		
		self.imgPath_0 = imgPath_0
		self.imgPath_1 = imgPath_1
		
		self.resolution = Image.open(imgPath_0).size
		
	def __len__(self):
		return 1

	def __getitem__(self, idx):

		INPUT_MEAN 	= [0.5 * 255, 0.5 * 255, 0.5 * 255]
		INPUT_STD 	= [0.5 * 255, 0.5 * 255, 0.5 * 255]

		try:
			img_0 		= cv2.imread(self.imgPath_0)
			img_0 		= img_0.astype(np.float32)
		except AttributeError:
			print("Failed to load " + imgPath_0)
			img_0 = np.ones((128,128,3)).astype(np.float32)
			
		try:
			img_1 		= cv2.imread(self.imgPath_1)
			img_1 		= img_1.astype(np.float32)
		except AttributeError:
			print("Failed to load " + imgPath_1)
			img_1 = np.ones((128,128,3)).astype(np.float32)
	
		self.width 	= img_0.shape[1]
		self.height = img_0.shape[0]

		newWidth 	= self.approxNumber(self.width)
		newHeight 	= self.approxNumber(self.height)
		
		img_0 = cv2.resize(img_0,(newWidth, newHeight))
		img_1 = cv2.resize(img_1,(newWidth, newHeight))

		#norm
		img_0 = tf.normalize(img_0, INPUT_MEAN, INPUT_STD)
		img_0 = torch.from_numpy(img_0).permute(2, 0, 1).contiguous().float()
		
		img_1 = tf.normalize(img_1, INPUT_MEAN, INPUT_STD)
		img_1 = torch.from_numpy(img_1).permute(2, 0, 1).contiguous().float()

		return torch.cat([img_1, img_0], dim=0)

	def getSize(self):
		return self.resolution
	
	def approxNumber(self, number):
		
		approx = 0
		
		while(number >= 16):
			
			b = 16
			oldb = 0
			
			while(number >= b):
				
				oldb = b
				b = b << 1
				
			approx += oldb
			number -= oldb
			
		return approx
