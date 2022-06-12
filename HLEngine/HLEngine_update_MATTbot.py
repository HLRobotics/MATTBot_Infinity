#@author:Akhil P Jacob
#HLRobotics-Automation
import git
import cv2
import subprocess
import sys

def update():
    try:
        git_dir = "../MATTBot_2021/"
        g = git.cmd.Git(git_dir)
        g.pull()
        return(True)
        
    except:
        return(False)







            


