#!/usr/bin/env python3

import requests 

URL			= "https://drive.google.com/uc?export=download"
OUTPUT		= "/home/Workspace/install/ckpt.zip"
CONTENT_ID 	= "1X7PWDY2nAx8ZeSLso5qeypRUCDokNFms"

if __name__ == "__main__":
	
	print("Requesting " + URL)
	
	session = requests.Session()

	response = session.get(URL, params={'id':CONTENT_ID})
	
	confirmToken = None
	
	for key, value in response.cookies.items():
		if key.startswith('download_warning'):
			confirmToken = value
			break
		
	print("Request data")
	
	response = session.get(URL, params={'id':CONTENT_ID, 'confirm':confirmToken})
	
	print("Response status code " + str(response.status_code))

	if(int(response.status_code) == 200):

		print("Writing content to file " + OUTPUT)

		f = open(OUTPUT, "wb")
		f.write(response.content)
		f.close()

		print("Done.")
	
	else:
		print("Download failed.")
