import os
import torch
import time
import argparse
import shutil
import numpy as np
import cv2
from os import path
import torch.backends.cudnn as cudnn
from core import models
from core import datasets
from core.utils.optim import Optim
from core.utils.config import Config
from core.utils.eval import EvalPSNR
from core.ops.sync_bn import DataParallelwithSyncBN
from myData import MyData
import time
import warnings
warnings.filterwarnings("ignore")

FULL_PATH_TO_CHECKPOINT = "/home/Workspace/install/models/voxelflow_finetune_model_best.pth.tar"
CONFIG_FILE = "/home/Workspace/install/configs/voxel-flow_finetune.py" 

# Parse commandline arguments 
def parse_args():
	parser = argparse.ArgumentParser(description='Train Voxel Flow')
	parser.add_argument('img1Path', help='path to first image')
	parser.add_argument('img2Path', help='path to first image')
	parser.add_argument('outPath', help='path to first image')
	args = parser.parse_args()
	return args

def betterMain():
	
	global cfg
	args = parse_args()
	cfg = Config.from_file(CONFIG_FILE)
		
	os.environ["CUDA_VISIBLE_DEVICES"] = '0'
	cudnn.benchmark = True
	cudnn.fastest = True

	model = getattr(models, cfg.model.name)(cfg.model).cuda()
	cfg.train.input_mean = model.input_mean
	cfg.train.input_std = model.input_std
	cfg.test.input_mean = model.input_mean
	cfg.test.input_std = model.input_std

	myData = MyData(args.img1Path, args.img2Path)

	val_loader = torch.utils.data.DataLoader(
		myData,
		batch_size=1,
		shuffle=False,
		num_workers=1,
		pin_memory=True)

	checkpoint = torch.load(FULL_PATH_TO_CHECKPOINT)
	model.load_state_dict(checkpoint['state_dict'], False)

	model = DataParallelwithSyncBN(model, device_ids=[0]).cuda()

	interpolate(model, val_loader, myData, args.outPath)
	
def interpolate(model, val_loader, data, outPath):
	
	with torch.no_grad():
		
		# switch to evaluate mode
		model.eval()

		length = len(val_loader)

		avgTime = 0
		totalNum = length

		for i, input in enumerate(val_loader):
			
			input_var = torch.autograd.Variable(input)
			
			output = model(input_var)
			pred = output.data.cpu().numpy()
			
			width = pred.shape[2]
			height = pred.shape[3]
			comp = 3
		
			img = np.ones((width, height, comp))
			
			for y in range(height):
				for x in range(width):
					for c in range(comp):
						img[x, y, c] = (pred[0, c, x, y] + 1) * 128
			
			if(img.max() < 10):
				print("\nFailed to interpolate frame " + str(i*2+1) + "-50")
				continue
			
			img = cv2.resize(img, data.getSize())
			cv2.imwrite(outPath, img)
			
