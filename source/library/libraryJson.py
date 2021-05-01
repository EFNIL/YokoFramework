import json
import sys
import re

def SetJSONObj(path, nameFile, flag, data):
	path += str("\\" + str(nameFile) + ".json")
	
	with open(path, flag, encoding = "utf-8") as f:
		json.dump(data, f, ensure_ascii = False, indent = 4)
		return True
	pass


def AddJSONObj(path, nameFile, flag, data):
	path += str("\\" + str(nameFile) + ".json")
	
	with open(path, 'r+', encoding = "utf-8") as f:
		d = json.load(f)
		d.append(data)
		f.seek(0)
		json.dump(d, f, ensure_ascii = False, indent = 4)
		return True
	pass

def GetJSONObj(path, nameFile):
	path += str("\\" + str(nameFile) + ".json")
	with open(path, 'r', encoding = "utf-8") as f:
	    data = json.load(f)
	    return data
	pass