import random

def GetUser(vk, IDUser, naming = 'nom'):
	return vk.users.get(user_ids = IDUser, name_case = naming)
	pass

#NOT WORK
def GetChat(vk, IDChat, naming = 'nom'):
	try:
		request = vk.messages.getConversationsById(peer_ids=IDChat)
		print(request)
		for response in request['items']:
		    chat_settings= response['chat_settings']
		    title= chat_settings['title']
		    print(title)
		return obj
	except:
		print('Error:\n', traceback.format_exc())
	pass

def GetChatNumber(vk, IDChat, naming = 'nom'):
	try:
		obj = vk.messages.getConversationMembers(peer_id = 2000000000 + IDChat, name_case = naming)
		return obj
	except:
		print('Error:\n', traceback.format_exc())
	pass

def CountUserChat(vk, IDChat):
	try:
		chatOb = GetChatNumber(vk, IDChat)
		return chatOb['count']
	except:
		print('Error:\n', traceback.format_exc())

def GetUserChat(vk, IDChat, naming = 'nom'):
	try:
		chatOb = GetChatNumber(vk, IDChat, naming)
		return chatOb['profiles']
	except:
		print('Error:\n', traceback.format_exc())

def RandomGetUserChat(vk, IDChat, naming = 'nom'):
	listp = GetUserChat(vk, IDChat)
	return listp[random.randint(0, len(listp) - 1)]

def SerchChatUserNameToID(vk, IDChat, fname = '', lname = '', naming = 'nom'):
	listp = GetUserChat(vk, IDChat, naming)
	listSearch = []
	for i in range(0, len(listp) - 1):
		if fname != '' and lname != '':
			if listp[i]['first_name'].lower() == fname.lower() and listp[i]['last_name'].lower() == lname.lower():
				listSearch.append(listp[i]['id'])
				break
		elif lname != '':
			if listp[i]['last_name'].lower() == lname.lower():
				listSearch.append(listp[i]['id'])
		elif fname != '':
			if listp[i]['first_name'].lower() == fname.lower():
				listSearch.append(listp[i]['id'])

	return (-1, listSearch)[len(listSearch) > 0]

def ShowChatUserName(vk, IDChat):
	listp = GetUserChat(vk, IDChat)
	for i in range(0, len(listp)):
		print(listp[i]['screen_name'])
	pass

def KickUser(vk, chatID, userID):
	try:
		vk.messages.removeChatUser(chat_id = chatID, user_id = userID, member_id = userID)
	except:
		print('Error:\n', traceback.format_exc())
	pass

def GetGroupUsers(vk, IDGroup):
	return vk.groups.getMembers(group_id = IDGroup, sort = 184722040, offset = 0)
	pass

def CheckUserInGroup(vk, IDGroup, IDUser):
	data = GetGroupUsers(vk, 184722040)
	for e in data['items']:
		if IDUser == int(e):
			return True
	return False