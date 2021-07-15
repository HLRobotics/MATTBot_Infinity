import serial
import smtplib
import os
rate=9600
import time
import bluetooth

def find_Port():
    try:
        ser = serial.Serial("COM1", rate)
        print("Connected to COM1")
        return('COM1')
    except:
        print("Disconnected to COM1")
    
    try:
        ser = serial.Serial("COM2", rate)
        print("Connected to COM2")
        return('COM2')
    except:
        print("Disconnected to COM2")

    
    try:
        ser = serial.Serial("COM3", rate)
        print("Connected to COM3")
        return('COM3')
    except:
        print("Disconnected to COM3")


    try:
        ser = serial.Serial("COM4", rate)
        print("Connected to COM4")
        return('COM4')
    except:
        print("Disconnected to COM4")

    try:
        ser = serial.Serial("COM5", rate)
        print("Connected to COM5")
        return('COM5')
    except:
        print("Disconnected to COM5")

    try:
        ser = serial.Serial("COM6", rate)
        print("Connected to COM6")
        return('COM6')
    except:
        print("Disconnected to COM6")


    try:
        ser = serial.Serial("COM7", rate)
        print("Connected to COM7")
        return('COM7')
    except:
        print("Disconnected to COM7")

    try:
        ser = serial.Serial("COM8", rate)
        print("Connected to COM8")
        return('COM8')
    except:
        print("Disconnected to COM8")

    try:
        ser = serial.Serial("COM9", rate)
        print("Connected to COM9")
        return('COM9')
    except:
        print("Disconnected to COM9")

    try:
        ser = serial.Serial("COM10", rate)
        print("Connected to COM10")
        return('COM10')
    except:
        print("Disconnected to COM10")

    try:
        ser = serial.Serial("COM11", rate)
        print("Connected to COM11")
        return('COM11')
    except:
        print("Disconnected to COM11")

    try:
        ser = serial.Serial("COM12", rate)
        print("Connected to COM12")
        return('COM12')
    except:
        print("Disconnected to COM12")

    try:
        ser = serial.Serial("COM13", rate)
        print("Connected to COM13")
        return('COM13')
    except:
        print("Disconnected to COM13")

    try:
        ser = serial.Serial("COM14", rate)
        print("Connected to COM14")
        return('COM14')
    except:
        print("Disconnected to COM14")

    try:
        ser = serial.Serial("COM15", rate)
        print("Connected to COM15")
        return('COM15')
    except:
        print("Disconnected to COM15")

    try:
        ser = serial.Serial("COM16", rate)
        print("Connected to COM16")
        return('COM16')
    except:
        print("Disconnected to COM16")

    try:
        ser = serial.Serial("COM17", rate)
        print("Connected to COM17")
        return('COM17')
    except:
        print("Disconnected to COM17")

    try:
        ser = serial.Serial("COM18", rate)
        print("Connected to COM18")
        return('COM18')
    except:
        print("Disconnected to COM18")

    try:
        ser = serial.Serial("COM19", rate)
        print("Connected to COM19")
        return('COM19')
    except:
        print("Disconnected to COM19")

    try:
        ser = serial.Serial("COM20", rate)
        print("Connected to COM20")
        return('COM20')
    except:
        print("Disconnected to COM20")

    try:
        ser = serial.Serial("/dev/ttyUSB0", rate)
        print("Connected to /dev/ttyUSB0")
        return('/dev/ttyUSB0')
    except:
        print("Disconnected to /dev/ttyUSB0")

    try:
        ser = serial.Serial("/dev/ttyACM0", rate)
        print("Connected to /dev/ttyACM0")
        return('/dev/ttyACM0')
    except:
        print("Disconnected to /dev/ttyACM0")


def serSend(port,rate,data):
    try:
        ser = serial.Serial(port, rate)
        time.sleep(2)
        ser.write(str.encode(str(data)))        
        return('HLEngine:data sent...')
    except:
        return ("HLEngine:issue with the  port")

def serRecieve(port,rate):
    try:
        ser = serial.Serial(port, rate)
        Serial_data = ser.readline()
        return (Serial_data)
    except:
        return ("HLEngine:issue with the  port")


def sendMail(mailid,psd,to,msg):
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(mailid,psd)
        content=msg
        server.sendmail(mailid,to,content)
        server.quit()
        return ("HLEngine :mail_sent")
    except:
        return ("HLEngine :failed to send mail")

def shutDown_windows():
    try:
        os.system("shutdown /s /t 1")
    except:
        return ("HLEngine :failed to shutdown windows")


def reboot_windows():
    try:
        os.system("restart /s /t 1")
    except:
        return ("HLEngine :failed to reboot windows")

def linux_shutdown():
    try:
        os.system("poweroff")
    except:
        return ("HLEngine :failed to shutdown linux")

def linux_boot():
    try:
        os.system("reboot")
    except:
        return ("HLEngine :failed to reboot linux")

def spy():
    try:
        os.system("sudo motion")
    except:
        return ("HLEngine :failed to configure motion")
def stop_spy():
    try:
        os.system("sudo service motion stop")
    except:
        return ("HLEngine :failed to shutdown windows")

def ifconfig():
    try:
        os.system("ifconfig")
    except:
        return ("HLEngine :sorry ,cmd error")

def automatA():
    try:
        os.system("chmod u+x automata.sh")
        os.system("./automata.sh")
    except:
        return ("HLEngine :cannot launch MATTAutomata")



def botAccess(bot_address):
    try:
        bd_addr=bot_address
        port = 1
        sock = bluetooth.BluetoothSocket (bluetooth.RFCOMM)
        sock.connect((bd_addr,port))
        print("Connection to robot VECTOR [established]")
        while 1:
            tosend = input('Enter your wireless command here:  ')
            if (tosend != 'exit'):
                sock.send(tosend)
                #return("data_send")
            elif (tosend=='exit'):
                break
    except:
        print("HLEngine: Connection to robot VECTOR [interrupted]")


def VECTORCONTROLLER_JOYSTICK():
    try:
        #os.system("chmod u+x joyStick.sh")
        os.system("./joyStick.sh")
    except:
        return ("HLEngine :cannot launch MATTAutomata")






