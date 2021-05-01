import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import threading
import startModule
import timerModule
import speachModule
import sendModule

tokenConfig, nameBot, version = startModule.InitializationFromConfig()

vk_session = vk_api.VkApi(token = tokenConfig)
longpoll = VkBotLongPoll(vk_session, 184722040)
vk = vk_session.get_api()

def GetMessage(vk, event):
	textMessage = event.obj.text
	typeMessage = ""
	chatID = ""
	fromID = event.obj.from_id

	if event.from_chat:
		typeMessage = 1
		chatID = event.chat_id
	elif event.from_user:
		typeMessage = 2
		chatID = event.obj.user_id

	return {"type" : typeMessage, "id" : chatID, "text" : textMessage, "attach" : '', 'fromid' : fromID}
	pass

def start():
	timerModule.start()
	speachModule.start();
	startModule.On(vk)
start()

def main():
	for event in longpoll.listen():
		# _command.basecommand(vk, event)
		if event.type == VkBotEventType.MESSAGE_NEW:
			data = GetMessage(vk, event)
			
			speachModule.main(data);
			sendModule.main(vk, event);

			if startModule.Off(vk, event):
				timerModule.off()
				return
main()
