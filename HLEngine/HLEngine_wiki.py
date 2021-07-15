#@author: Akhil P Jacob
#HLRobotics-Automation
import wikipedia


def wiki(param):
    try:
        return(wikipedia.summary(param))
    except:
        return ("HLEngine:error in executing wiki....")



