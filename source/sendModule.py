import random
import copy

from library import vkLibrary

def SendMassagesBase(vk, peer, user, answer = '', attach = ''):
	try:
		vk.messages.send(peer_id = peer, user_id = user, message = answer, attachment = attach, random_id = random.randint(1, 2147483647))
	except:
		print('Error:\n', traceback.format_exc())

def SendMassagesOnIDUser(vk, event, user, answer = '', attach = ''):
    try:
        vk.messages.send(peer_id = event.obj.peer_id, 
                            user_id = user, 
                            message = answer, 
                            attachment = attach,
                            random_id = random.randint(1, 2147483647))
    except:
        print('Error:\n', traceback.format_exc())
    pass

def SendMassagesOnIDChat(vk, event, chat, answer = '', attach = ''):
    try:
        vk.messages.send(conversation_message_id = event.obj.conversation_message_id, 
                            chat_id = chat, 
                            message = answer,
                            attachment = attach,
                            random_id = random.randint(1, 2147483647))
    except:
        print('Error:\n', traceback.format_exc())
    pass

def SendMessage(vk, event, messageData):
	if messageData['type'] == 1:
		SendMassagesOnIDChat(vk, event, messageData['id'], messageData['text'], messageData['attach'])
	elif messageData['type'] == 2:
		SendMassagesOnIDUser(vk, event, messageData['id'], messageData['text'], messageData['attach'])

def CopyDict(d):
    t = copy.deepcopy(d)
    return t

LIST_SEND_MESSAGE = []
def Add(messageData, valueText):
    if valueText != "":
        t = copy.deepcopy(messageData)
        t['text'] = valueText
        LIST_SEND_MESSAGE.append(t)

def CheckUserInGroup(messageData, vk):
    if vkLibrary.CheckUserInGroup(vk, 184722040, messageData['fromid']):
        return True
    else:
        return False

def main(vk, event):
    for i in range(0, len(LIST_SEND_MESSAGE)):
        if CheckUserInGroup(LIST_SEND_MESSAGE[i], vk):
            SendMessage(vk, event, LIST_SEND_MESSAGE[i])
        else:
            LIST_SEND_MESSAGE[i]['text'] = "Для активации бота нужно подписаться\nhttps://vk.com/yokobot"
            SendMessage(vk, event, LIST_SEND_MESSAGE[i])
            break
    LIST_SEND_MESSAGE.clear()