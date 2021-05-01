import random
import numpy
import re
import difflib

def getAppeal():
	return ', '.join(appeal)

def tanimoto(s1, s2):
	a, b, c = len(s1), len(s2), 0.0

	for sym in s1.lower():
		if sym in s2.lower():
			c += 1

	return c / (a + b - c)

def CheckAppeal(message):
	listWords = message['text'].split(' ')

	for ap in appeal:
		if ap.lower() == listWords[0].lower():
			return True

	return False

def CutAppeal(message):
	listWords = message['text'].split(' ')
	for ap in appeal:
		if ap.lower() == listWords[0].lower():
			del listWords[0]
			return ' '.join(listWords)

def ClearCharMessage(message, listChar):
    result = message
    for char in listChar:
        result = result.replace(char, '')
    return result

def RandomChoose(words):
    count = len(words)
    randomIndex = random.randint(0, count - 1)
    return words[randomIndex]

def CheckWordPosition(message, word, position):
	listWords = message['text'].split(' ')
	if word == listWords[position]:
		return True
	return False

def CheckEqualAtOnce(message, targetword):
	listWords = message.split(' ')
	listTarget = targetword.split(' ')
	countDone = 0

	for words in listWords:
		if difflib.SequenceMatcher(None, words.lower(), listTarget[countDone].lower()).ratio() > 0.7:
			if countDone < len(listTarget) - 1:
				countDone += 1
			else:
				return True
	return False

def CheckEqual(message, targetword):
	return CheckEqualAtOnce(message['text'], targetword);

def CheckMultyEqual(message, targetwords):
	for word in targetwords:
		if CheckEqual(message, word):
			return True
	return False

# 'a b c d e', 0, 2 -> d e
def CutRangeInner(message, startpos, endpos):
	listWords = message['text'].split(' ')
	for i in range(startpos, endpos + 1):
		del listWords[i]
	return ' '.join(listWords)

# 'a b c d e', 0, 2 -> a b c
def CutRangeOuter(message, startpos, endpos):
	listWords = message['text'].split(' ')
	tempList = []
	for i in range(startpos, endpos + 1):
		tempList.append(listWords[i])
	return ' '.join(tempList)

# 'a b c d e', 0 ->  b c d e
def CutPosition(message, delpos):
	listWords = message.split(' ')
	del listWords[delpos]
	return ' '.join(listWords)

def CutMultyPosition(message, listdelpos):
	listWords = message['text'].split(' ')
	for pos in listdelpos:
		del listWords[pos]
	return ' '.join(listWords)

def GetPositionWords(message, word):
	listWords = message.split(' ')
	listIndex = []
	for i in range(0, len(listWords)):
		if listWords[i] == word:
			listIndex.append(i)
	return listIndex

def CutAllEntry(message, target):
	listWords = message['text'].split(' ')
	for word in listWords:
		if word.lower() == target.lower():
			listWords.remove(word)
	return ' '.join(listWords)

def CutWords(message, word):
	listWords = message['text'].split(' ')
	for w in listWords:
		if w == word:
			listWords.remove(w)
			return listWords

def CutPhrase(baseText, cutText):
    if isinstance(cutText, (list, tuple, numpy.ndarray)):
        text = baseText['text'].lower()
        for i in range(0, len(cutText)):
            text = re.sub(r'%s' %cutText[i].lower() ,' ', text)            
        return text
    elif isinstance(cutText, str):
        return re.sub(r'%s' %cutText.lower(), ' ', baseText['text'].lower())
    pass

def ReplaceWords(message, wordReplase, wordNew):
	listWords = message.split(' ')
	allIndex = GetPositionWords(message, wordReplase)

	for i in range(0, len(allIndex)):
		listWords[allIndex[i]] = wordNew
	return ' '.join(listWords)

# print(GetPositionWords('русская рулетка ? ! хаха !', "!"))
# "да?", "согласна?", "не?", "нет?", "не согласна?", "правда?", "же?"
# print(CheckEqualAtOnce("Й привет как дела?", "да?"))
# print(CheckEqualAtOnce("Й привет как дела? ! .", "Й привет как дела ?"))
# print(ClearCharMessage("Й привет как дела?", "?"))
