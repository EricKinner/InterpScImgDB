#!/usr/bin/env python3

import requests 
  
URL="https://drive.google.com/uc?export=download&id=1FB-mpS4UokiLriDBNJSBmozMQRH0Qez1"
OUTPUT="/home/Workspace/install/models/voxelflow_finetune_model_best.pth.tar"
  
if __name__ == "__main__":
	
	print("Requesting " + URL)
	
	response = requests.get(URL)

	print("Response status code " + str(response.status_code))

	if(int(response.status_code) == 200):

		print("Writing content to file " + OUTPUT)

		f = open(OUTPUT, "wb")
		f.write(response.content)
		f.close()

		print("Done.")
	
	else:
		print("Download failed.")
