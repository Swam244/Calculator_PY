import threading
import pyttsx3

class sub_thread(threading.Thread):
    wordlist = []
    def __init__(self,args=''):
        threading.Thread.__init__(self)
        self.wordlist.append(args)
    def Speak(self):
        engine = pyttsx3.init()
        l = engine.getProperty('voices')
        engine.setProperty('voice',l[1].id)
        for i in self.wordlist:
            engine.say(i)
        engine.runAndWait()

    def run(self):
        self.Speak()