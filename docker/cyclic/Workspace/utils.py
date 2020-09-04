import shutil
import os

def getFileExtension(filename):
	
	lastDot = filename.rfind(".")
	
	return filename[lastDot:]

def getFileNameWithoutExtension(filename):
	
	lastDot = filename.rfind(".")
	
	return filename[:lastDot]

def filterImages(fileList):
	
	result = []
	
	for filename in fileList:
		
		lowfileName = filename.lower()

		if lowfileName.endswith(".png") or lowfileName.endswith(".jpg") or lowfileName.endswith(".jpeg"):
			result.append(filename)
	
	return result

def deleteAllFiles(orig):
	
	fileList = os.listdir(orig)
	
	for fileElem in fileList:
		
		if(os.path.isdir(os.path.join(orig, fileElem))):
			continue
		
		oldPath = os.path.join(orig, fileElem)
		
		os.remove(oldPath)

def moveAllFiles(orig, dest):
	
	fileList = os.listdir(orig)
	
	for fileElem in fileList:
		
		if(os.path.isdir(os.path.join(orig, fileElem))):
			continue
		
		oldPath = os.path.join(orig, fileElem)
		newPath = os.path.join(dest, fileElem)
		
		shutil.move(oldPath, newPath)
		
def copyAllFiles(orig, dest):
	
	fileList = os.listdir(orig)
	
	for fileElem in fileList:
		
		if(os.path.isdir(os.path.join(orig, fileElem))):
			continue
		
		oldPath = os.path.join(orig, fileElem)
		newPath = os.path.join(dest, fileElem)
		
		shutil.copyfile(oldPath, newPath)
