#@author:Akhil P Jacob
#HLRobotics-Automation
import git
import cv2
import subprocess
import sys

def update():
    try:       
        print("HLEngine:updating MATTBot 2020......")
        git_dir = "../../../MATTBot/"
        g = git.cmd.Git(git_dir)
        g.pull()
        return("HLEngine:MATTbot updated, reboot MATT to reflect ......")
        
    except:
        return("HLEngine:cannot connect to MATTBot Server")







            


