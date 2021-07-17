'''
HLDynamic Integrations 2020
Author:Er.Akhil P Jacob
CONCIOUSNESS
last updated on 10/05/2020
'''
import random
import string
import os
from HLEngine import HLEngine_Progressbar
from HLEngine import HLEngine_wordX
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_communications
from HLEngine import HLEngine_ImageProcessing
from Seeker import taskMapping
from Seeker import timeMapper


def introduction(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.INTRODUCTION:
            HLEngine_audioProcess.playsound("voice/myself.wav")
            HLEngine_audioProcess.playsound("voice/purpose1.wav")


def purpose(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.PURPOSE:
            HLEngine_audioProcess.playsound("voice/purpose2.wav")




def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in taskMapping.GREETING_INPUTS:
            HLEngine_audioProcess.playsound("voice/service.wav")
            return random.choice(taskMapping.GREETING_RESPONSES)



def bye(sentence):
 
    for word in sentence.split():
        if word.lower() in taskMapping.SIGNING_INPUT:
            HLEngine_Progressbar.progress("MATT down")
            HLEngine_audioProcess.playsound("voice/bye.wav")
            return ("off")

def utilCOM(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.SERIAL_MODE:
            try:   
                HLEngine_audioProcess.playsound("voice/wait.wav")             
                PORT=MATTbot_Engine.commonProtocols()
                return(PORT)
            except:
                print("Consciousness ERROR")

def EmotionDetector(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.EMOTIONS:
            HLEngine_audioProcess.playsound("voice/wait.wav") 
            result=MATTbot_Engine.sentimentalAnalsys(sentence)
            if(result<0):
                HLEngine_audioProcess.playsound("voice/sad.wav")
                return random.choice(taskMapping.EMOTION_OUT_SAD)
            elif(result>0):
                HLEngine_audioProcess.playsound("voice/happy.wav")
                return random.choice(taskMapping.EMOTION_OUT_HAPPY)
            else:
                return random.choice(taskMapping.EMOTIONS_NO)


def hyperLogic(param):
    for word in param.split():
        if word.lower() in taskMapping.questions:
            HLEngine_Progressbar.progress("Gathering")
            data=HLEngine_wordX.EW(param)
            xlogic=MATTbot_Engine.gainWisdom(data)
            HLEngine_audioProcess.playsound("voice/dataHere.wav") 
            f=open("hiveMind/hiveMind.txt","a")
            f.write(xlogic)
            f.close()
            #HLEngine_audioProcess.playsound("voice/burn.wav") 
            return(xlogic)


            
def down(sentence): 
    for word in sentence.split():
        if word.lower() in taskMapping.SHUTDOWN:
            HLEngine_Progressbar.progress("shutting down System")
            HLEngine_audioProcess.playsound("voice/bye.wav")
            HLEngine_communications.linux_shutdown()
            return("shutdown")

def reboot(sentence): 
    for word in sentence.split():
        if word.lower() in taskMapping.REBOOT:
            HLEngine_Progressbar.progress("rebooting")
            HLEngine_audioProcess.playsound("voice/reboot.wav")
            HLEngine_communications.linux_boot()
            return("reboot")

            
def soundCloud(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.SOUND_CLOUD_HITS: 
            HLEngine_Progressbar.progress("Opening Browser")           
            link=random.choice(taskMapping.SOUND_CLOUD)
            import webbrowser
            webbrowser.open(link, new=2)


def facebook(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.FACEBOOK:
            HLEngine_Progressbar.progress("Initializing")
            import webbrowser
            link="www.facebook.com"
            webbrowser.open(link, new=2)


def youtube(sentence):
    for word in sentence.split():
        if word.lower() in taskMapping.YOUTUBE:
            HLEngine_Progressbar.progress("Initializing")
            import webbrowser
            link="www.youtube.com"
            webbrowser.open(link, new=2)


def radioMango(param):
    for word in param.split():
        if word.lower() in taskMapping.RADIO_MANGO:
            HLEngine_Progressbar.progress("Initializing")
            import webbrowser
            link="https://onlineradiofm.in/stations/mango"
            webbrowser.open(link, new=2) 


def akashavani(param):  
    for word in param.split():
        if word.lower() in taskMapping.AKASHA_VANI:
            HLEngine_Progressbar.progress("Initializing")
            import webbrowser
            link="https://onlineradiofm.in/stations/fm-rainbow"
            webbrowser.open(link, new=2)

def clubFM(param):
    for word in param.split():
        if word.lower() in taskMapping.CLUB_FM:
            HLEngine_Progressbar.progress("Initializing")
            import webbrowser
            link="https://onlineradiofm.in/stations/club"
            webbrowser.open(link, new=2)









                    






                    



