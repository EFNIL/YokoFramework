from library import textLibrary
from library import libraryJson
from library import libraryIO
from library import vkLibrary

import timerModule
import sendModule
import copy

modules = {'send': sendModule, 'textlib': textLibrary, 'vklib': vkLibrary, 'timer' : timerModule, 'libio' : libraryIO, 'libjson' : libraryJson}

LIST_PHRASE = []
LIST_ANSWER = []
ANSWER = ""

class Phrase:
    keyword = []
    answer = []

    def __init__(self, keyword, answer):
        self.keyword = keyword
        self.answer = answer
        LIST_PHRASE.append(self)
    
    def Check(self, message):
        global ANSWER
        if textLibrary.CheckMultyEqual(message, self.keyword):
            Add(textLibrary.RandomChoose(self.answer))
            return True
        return False
        pass

def ClearMessage(message):
    listChar = [',', '?', '!']
    result = message
    for char in listChar:
        result = result.replace(char, '')
    return result

def Add(text):
    global LIST_ANSWER
    LIST_ANSWER.append(text)

def Combain(message, module):
    global ANSWER
    global LIST_ANSWER

    for i in range(0, len(LIST_ANSWER)):
        if i > 0:
            ANSWER += "" + LIST_ANSWER[i].lower()
        else:
            ANSWER += LIST_ANSWER[i]

        if i % 2 == 0 and len(LIST_ANSWER) - 1 != i:
            ANSWER += ', '
        elif i % 2 == 1 or len(LIST_ANSWER) - 1 == i:
            ANSWER += '. '

        # if len(LIST_ANSWER) - 1 > i:

    if ANSWER != "":
        # print(ANSWER)
        module['send'].Add(message, ANSWER)
        LIST_ANSWER = []
        ANSWER = ""
    pass

def start():
    data = libraryJson.GetJSONObj(libraryIO.CutFolderPath('source'), 'speach_core')
    for e in data['command']:
        Phrase(e['keyword'], e['answer'])

def main(message):
    messageTemp = copy.deepcopy(message)
    messageTemp['text'] = ClearMessage(message['text'])

    global ANSWER
    for e in LIST_PHRASE:
        e.Check(messageTemp)
    Combain(messageTemp, modules)