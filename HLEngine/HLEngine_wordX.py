#@author:Akhil P Jacob
#HLRobotics-Automation
import base64
def FW(param):
    try:
        sent=str(param)
        first, *middle, last = sent.split()
        #print(first, last)
        return(first)
    except:
        return("HLEngine:Error in excuting FW.....")

def EW(param):
    try:
        sent=str(param)
        first, *middle, last = sent.split()
        #print(first, last)
        return(last)
    except:
        return ("HLEngine:error in executing EW....")

def Image_decode(location):
    try:
        from PIL import Image, ImageEnhance, ImageFilter
        import pytesseract
        import os
        path = location
        img = Image.open(path)
        img = img.convert('RGBA')
        pix = img.load()
        text = pytesseract.image_to_string(Image.open(path))
        #os.remove('temp.jpg')
        return (text)
    except:
        return ("HLEngine:File missing...contact HLadmin")