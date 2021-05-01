import os
import datetime
import threading

from time import sleep

def Min2Sec(m):
    return m * 60

def Hour2Sec(h):
    return Min2Sec(60 * h)

def Day2Sec(d):
    return Hour2Sec(24 * d)

def Data2FullSec(dd, hh, mm, ss):
    return Day2Sec(dd) + Hour2Sec(hh) + Min2Sec(mm) + ss

class Timer:
    name = ""
    offsetSeconds = 0
    timeEnd = 0
    loop = False
    pause = False
    func = None

    def InitTimer(self):
        now = datetime.datetime.now()
        self.timeEnd = now + datetime.timedelta(seconds = self.offsetSeconds)

    def __init__(self, seconds, loop, func = None):
        LIST_TIMER.append(self)
        self.offsetSeconds = seconds
        self.loop = loop
        self.InitTimer()
        self.func = func
        pass

    def CheckTimeEvent(self):
        ss = self.timeEnd.second <= datetime.datetime.now().second
        mm = self.timeEnd.minute <= datetime.datetime.now().minute
        hh = self.timeEnd.hour <= datetime.datetime.now().hour
        dd = self.timeEnd.day <= datetime.datetime.now().day
        mn = self.timeEnd.month <= datetime.datetime.now().month
        ya = self.timeEnd.year <= datetime.datetime.now().year

        if ss and mm and hh and dd and mn and ya:
            return True
        return False
        pass

    def Active(self, ttime):
        print(datetime.datetime.now(), "\t|\t", self.timeEnd, ' <' + self.name)
        if self.pause:
            self.timeEnd += datetime.timedelta(ttime)

        if self.CheckTimeEvent():
            print('timer end')
            

            if self.loop:
                print("restarting timer...")
                self.InitTimer()
            else:
                LIST_TIMER.remove(self)

            if self.func != None:
                self.func()
        
            return True
        return False

    def Pause(self):
        if not self.pause:
            self.pause = True
        return self.pause

    def Continue(self):
        if self.pause:
            self.pause = False
        return self.pause

    def Reset(self):
        self.InitTimer()

    def Complete(self):
        self.timeEnd = datetime.datetime.now()
        pass

    def ToJSONObj(self):
        return { 'name' : self.name, 'offsetSeconds' : self.offsetSeconds,
                'timeEnd' : self.timeEnd, 'loop' : self.loop, 'pause' : self.pause }

    def CheckComplite(self):
        now = datetime.datetime.now()
        if now >= timeEnd:
            return True
        else:
            return False

LIST_TIMER = []
UPDATE_TIME = 1
IS_STOP = False

def updatetimers(name):
    global IS_STOP
    try:
        while not IS_STOP:
            for t in LIST_TIMER:
                t.Active(UPDATE_TIME)
            # print('T', threading.active_count())
            sleep(UPDATE_TIME)
            # print("\n")
    except Exception as e:
        print('Error:\n', traceback.format_exc())

mainthread = None
def start():
    global mainthread
    mainthread = threading.Thread(target = updatetimers, args = (1, ), daemon = False)
    mainthread.start()

def off():
    global IS_STOP
    IS_STOP = True