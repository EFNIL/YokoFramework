import os
import sys
import re

import numpy as np
import random

def CutFolderPath(folder):
	result = ""
	listFolder = sys.path[0].split('\\')

	for element in listFolder:
		if element != folder:
			result += element + "\\"
		else:
			result = result[0 : len(result) - 1]
			break
	
	return result

def CreateFolder(name):
	if not os.path.exists(name):
		os.mkdir(name)
		return True
	else:
		return False
	pass

def ExistFolder(name):
	if os.path.exists(name):
		return True
	else:
		return False

def ExistFile(name):
	if os.path.isfile(name):
		return True
	else:
		return False

#import old bot lib func
def FileExist(folder, nameFile, formt):
	path = re.sub(r'\b\\source\b', '', sys.path[0])
	path += "\\" + str(folder) + "\\" + str(nameFile) + str(formt)

	if os.path.isfile(path):
		return True
	else:
		return False

def GetPath(folder, nameFile, formt):
	path = re.sub(r'\b\\source\b', '', sys.path[0])
	path += "\\" + str(folder) + "\\" + str(nameFile) + str(formt)
	return path

def WriteText(folder, nameFile, flag, text):
	path = re.sub(r'\b\\source\b', '', sys.path[0])
	path += str("\\" + "data" + "\\" + str(folder) + "\\" + str(nameFile) + ".txt")

	f = open(path, flag)
	f.write(str(text) + "\n")
	f.close()
	pass

def ReadText(folder, nameFile, flag = 'r'):
	path = re.sub(r'\b\\source\b', '', sys.path[0])
	path += str("\\" + "data" + "\\" + str(folder) + "\\" + str(nameFile) + ".txt")

	f = open(path, flag)
	st = f.read()
	f.close()
	return st

def SearchInFileText(folder, nameFile, searchText):
	path = re.sub(r'\b\\source\b', '', sys.path[0])
	path += str("\\" + "data" + "\\" + str(folder) + "\\" + str(nameFile) + ".txt")

	f = open(path)
	
	for x in f:
		if x == str(searchText) + "\n" or x == str(searchText):
			f.close()
			return True
	f.close()

	return False