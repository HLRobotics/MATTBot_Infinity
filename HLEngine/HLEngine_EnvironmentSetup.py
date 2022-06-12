#@author:Er.Akhil P Jacob
#HLEngine Environmental settings
import subprocess
import sys
import time
def setup_libraries():
    print("\nWelcome to HL_ENGINE Development Platform 2020 - Robot Development Simplified")
    time.sleep(1)
    print("\nDesigned and Developed by: Er.Akhil P Jacob (last updated on 24th March 2020)")
    time.sleep(1)
    print("\nThe Setup will take time depending on the internet speed and the system performance.")
    print("\nIt is recommended to close all other applications including Editors or IDE's on installation")
    from xml.dom import minidom
    mydoc = minidom.parse('payload_setup.xml')
    payload = mydoc.getElementsByTagName('payload')    
    xfile=open("log.txt","w")
    xfile.write("")
    xfile.close()    
    for elem in payload:
        print(elem.firstChild.data)
        package = str(elem.firstChild.data)
        try:
            print("HLEngine : Commencing installation......")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except:
            print("HLEngine: Installation failed....")
            xfile=open("log.txt","a")
            xfile.write(package)
            xfile.close()



setup_libraries()
