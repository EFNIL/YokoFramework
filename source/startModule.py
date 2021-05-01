import sendModule
import timerModule

from library import libraryJson
from library import libraryIO

id_creator = int(libraryJson.GetJSONObj(libraryIO.CutFolderPath("source"), "config")['id_creator'] )

def InitializationFromConfig():
	if libraryIO.ExistFile(libraryIO.CutFolderPath("source") + "\\config.json"):
		data = libraryJson.GetJSONObj(libraryIO.CutFolderPath("source"), "config")
	else:
		libraryJson.SetJSONObj(libraryIO.CutFolderPath("source"), "config", 'w+', {
														    "token": "-1",
														    "name": "Yoko Nyan",
														    "version": "0.1",
														    "id_creator" : 382233116})
		data = libraryJson.GetJSONObj(libraryIO.CutFolderPath("source"), "config")
	
	return data['token'], data['name'], data['version']

def On(vk):
    try:
    	if not vk.groups.getOnlineStatus(group_id = '184722040')['status'] == "online":
            vk.groups.enableOnline(group_id = '184722040')
    	sendModule.SendMassagesBase(vk, id_creator, id_creator, "Включено")
    	print("ON")
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
    pass

def Off(vk, event):
    command = event.obj.text.lower()
    if event.from_user:
        if event.obj.from_id == id_creator and (command == 'выкл' or command == 'офф'):
            try:
            	if vk.groups.getOnlineStatus(group_id = '184722040')['status'] == "online":
            		vk.groups.disableOnline(group_id = '184722040')
            		print("OFF")
            except:
                pass
            
            sendModule.SendMassagesOnIDUser(vk, event, id_creator, "Выключено")
            return True
    elif event.from_chat:
        if event.obj.from_id == id_creator and (command == 'выкл' or command == 'офф'):
            try:
                if vk.groups.getOnlineStatus(group_id = '184722040')['status'] == "online":
                	vk.groups.disableOnline(group_id = '184722040')
                	print("OFF")
            except:
                pass

            sendModule.SendMassagesOnIDChat(vk, event, event.chat_id, "Выключено")
            return True
    return False