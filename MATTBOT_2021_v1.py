"""
Developed by Akhil P Jacob
HLRobotics and Software Automation 2021

"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import os
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_wiki
from HLEngine import HLEngine_communications
import requests
from Seeker import PortFinder
from Seeker import timeMapper
HLEngine_audioProcess.playAudio("Reminders\WELCOME2.mp3")
import sqlite3
import time
import serial
global TIME
TIME=0
config=open('user.matt','r')
USER=config.read()
USER=USER.split(",")
config.close()



class MATTBOT(object):
    def mattbot(self, Dialog):       
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 279)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"Design/MattBot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        #Dialog.setStyleSheet("background-color: rgb(235, 228, 228);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 261))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label.setStyleSheet("color: rgb(85, 0, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 151, 17))
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 30, 331, 25))
        self.lineEdit_2.setStyleSheet("color: rgb(164, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 60, 111, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit.setGeometry(QtCore.QRect(10, 30, 121, 26))
        self.timeEdit.setObjectName("timeEdit")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(370, 10, 91, 16))
        self.label_12.setStyleSheet("color: rgb(204, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(10, 60, 121, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(140, 60, 111, 25))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 60, 91, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 461, 131))
        self.listWidget.setStyleSheet("color: rgb(92, 53, 102);")
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 20, 251, 25))
        self.lineEdit_5.setStyleSheet("color: rgb(52, 101, 164);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 341, 161))
        self.textEdit.setStyleSheet("color: rgb(204, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 110, 111, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 80, 111, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(360, 20, 111, 25))
        self.comboBox.setStyleSheet("color: rgb(32, 74, 135);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(360, 140, 111, 25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 170, 111, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setGeometry(QtCore.QRect(360, 200, 111, 25))
        #self.pushButton_14.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setGeometry(QtCore.QRect(360, 50, 111, 25))
        #self.pushButton_15.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(220, 10, 67, 17))
        self.label_8.setStyleSheet("color: rgb(164, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 67, 17))
        self.label_9.setStyleSheet("color: rgb(32, 74, 135);")
        self.label_9.setObjectName("label_9")
        self.dial_2 = QtWidgets.QDial(self.tab_5)
        self.dial_2.setGeometry(QtCore.QRect(20, 40, 171, 121))
        self.dial_2.setObjectName("dial_2")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(110, 10, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(300, 10, 67, 17))
        self.label_11.setObjectName("label_11")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 10, 89, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit.setGeometry(QtCore.QRect(160, 180, 211, 25))
        self.lineEdit.setStyleSheet("color: rgb(85, 0, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.dial_3 = QtWidgets.QDial(self.tab_5)
        self.dial_3.setGeometry(QtCore.QRect(200, 40, 171, 121))
        self.dial_3.setObjectName("dial_3")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(10, 180, 131, 17))
        self.label_13.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 180, 86, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_8.setGeometry(QtCore.QRect(380, 40, 89, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_9.setGeometry(QtCore.QRect(380, 70, 89, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_10.setGeometry(QtCore.QRect(380, 100, 89, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_11.setGeometry(QtCore.QRect(380, 130, 89, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 67, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 10, 351, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 50, 351, 25))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 67, 17))
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 160, 351, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox.setGeometry(QtCore.QRect(90, 80, 341, 23))
        self.checkBox.setStyleSheet("color: rgb(32, 74, 135);")
        self.checkBox.setObjectName("checkBox")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 120, 351, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(210, 10, 256, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 191, 201))
        self.label_7.setStyleSheet("border-image: url(Design/MattBot.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_3, "")

        ''' Time'''
        self.timer = QtCore.QTimer(Dialog)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()
        self.dateEdit.setDate(QDate.currentDate())

        ''' Startups'''
        conn = sqlite3.connect('DATABASE/MATTBOT2.db')  
        cursor = conn.cursor()
        query="SELECT * from REMINDERS"        
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall();    
        #print(result)        
        listbro=[]
        listbro.clear()   
        for i in result:            
            a=str(i)[1:-1]
            listbro.append(a)  
        self.listWidget.clear()
        for i in listbro:            
            self.listWidget.addItem(i)
        listbro.clear()
        conn.close()

        self.dial_2.setMaximum(100)
        self.dial_2.setMinimum(0)
        self.dial_2.setValue(100)
        self.dial_2.valueChanged.connect(self.lightAnalog)

        self.dial_3.setMaximum(100)
        self.dial_3.setMinimum(0)
        self.dial_3.setValue(100)
        self.dial_3.valueChanged.connect(self.fanAnalog)

        self.pushButton.clicked.connect(self.ADD_REMINDER)
        self.pushButton_2.clicked.connect(self.REMOVE_ALL_REMINDERS)
        self.pushButton_3.clicked.connect(self.DELETE_REMINDER)
        self.pushButton_4.clicked.connect(self.ADDUSER)
        self.pushButton_8.clicked.connect(self.fanON)
        self.pushButton_9.clicked.connect(self.fanOFF)
        self.pushButton_10.clicked.connect(self.lightsON)
        self.pushButton_11.clicked.connect(self.lightsOFF)
        self.pushButton_7.clicked.connect(self.Send)
        self.pushButton_15.clicked.connect(self.LANTALK)
        self.pushButton_6.clicked.connect(self.Message_Sent)
        self.pushButton_12.clicked.connect(self.READ)
        self.pushButton_13.clicked.connect(self.CLEAR)


        try:
            self.lineEdit_3.setText(USER[0])
            self.lineEdit_4.setText(USER[1])
            #print(USER[2])
            if(USER[2]=="Linux OS"):              
                self.comboBox_3.setCurrentIndex(2)
            elif(USER[2]=="Windows OS"):              
                self.comboBox_3.setCurrentIndex(1)
            elif(USER[2]=="Mac OS"):               
                self.comboBox_3.setCurrentIndex(3)
            else:
                self.comboBox_3.setCurrentIndex(0)
            if (USER[3]=="True"):                
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
        except:
            self.lineEdit_3.setText("Enter your NAME")
            self.lineEdit_4.setText("Enter your mail ID")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def CLEAR(self):
        self.textEdit.setText("")
        msg=QMessageBox()
        msg.setWindowTitle("MATTBot 🤖")
        msg.setText(str("CLEARED")) 
        x = msg.exec_()

    def READ(self):
        try:
            data=self.textEdit.toPlainText()            
            HLEngine_audioProcess.readText(str(data))
            
        
        except:
            #HLEngine_audioProcess.readText("Sorry. cannot read")
            msg=QMessageBox()
            msg.setWindowTitle("MATTBot 🤖")
            msg.setText(str("SORRY😟 CANNOT READ"))       
            x = msg.exec_()
        

    def Message_Sent(self):      
        reciever=self.comboBox.currentText()    
        if(reciever=="BOT"):   
            query=self.lineEdit_5.text()
            response=HLEngine_wiki.wiki(query)
            self.textEdit.setText(response)

            
    def fanON(self):
        protocol=self.comboBox_2.currentText()
        if(protocol=='IP'):
            ip=self.lineEdit.text()
            URL="http://"+ip+"/MOTOR=ON/"
            try:
                r = requests.post(url = URL)
            except:
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Cooler On"))       
                x = msg.exec_()
        if(protocol=='Serial'):            
            config="/MOTOR=ON/"
            try:
                ser=PortFinder.FindPort()
                self.lineEdit.setText(ser)
                ser.write(str.encode(str(config))) 
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Cooler On"))       
                x = msg.exec_()
            except:
                self.lineEdit.setText("MATTWARE Not Connected") 
                
   
    def fanOFF(self):
        protocol=self.comboBox_2.currentText()
        if(protocol=='IP'):
            ip=self.lineEdit.text()
            URL="http://"+ip+"/MOTOR=OFF/"
            try:
                r = requests.post(url = URL)
            except:
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Cooler Off"))       
                x = msg.exec_()

        if(protocol=='Serial'):            
            config="/MOTOR=OFF/"
            try:
                ser=PortFinder.FindPort()
                self.lineEdit.setText(ser)
                ser.write(str.encode(str(config))) 
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Cooler Off"))       
                x = msg.exec_()
            except:
                self.lineEdit.setText("MATTWARE Not Connected") 
                
                
    def lightsON(self):
        protocol=self.comboBox_2.currentText()
        if(protocol=='IP'):
            ip=self.lineEdit.text()
            URL="http://"+ip+"/LED=ON/"
            try:
                r = requests.post(url = URL)
            except:
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Lights On"))       
                x = msg.exec_()

        if(protocol=='Serial'):            
            config="/LED=ON/"
            try:
                ser=PortFinder.FindPort()
                self.lineEdit.setText(ser)
                ser.write(str.encode(str(config))) 
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Lights On"))       
                x = msg.exec_()
            except:
                self.lineEdit.setText("MATTWARE Not Connected") 
                

    def lightsOFF(self):
        protocol=self.comboBox_2.currentText()
        if(protocol=='IP'):
            ip=self.lineEdit.text()
            URL="http://"+ip+"/LED=OFF/"
            try:
                r = requests.post(url = URL)
            except:
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Lights Off"))       
                x = msg.exec_()

        if(protocol=='Serial'):            
            config="/LED=OFF/"
            try:
                ser=PortFinder.FindPort()
                self.lineEdit.setText(ser)
                ser.write(str.encode(str(config))) 
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Lights Off"))       
                x = msg.exec_()
            except:
                self.lineEdit.setText("MATTWARE Not Connected") 
                

    def lightAnalog(self):
        IntensityData=self.dial_2.value()    
        self.label_10.setText(str(IntensityData))    
   
    
    def fanAnalog(self):
        SpeedData=self.dial_3.value()
        self.label_11.setText(str(SpeedData))

    def Send(self):
        protocol=self.comboBox_2.currentText()
        if(protocol=='IP'):
            IntensityData=self.dial_2.value() 
            SpeedData=self.dial_3.value() 
            if(IntensityData<=100 and IntensityData>75):
                intensity=100   
                config="/L100/"         
            elif(IntensityData<=75 and IntensityData>50):
                intensity=75
                config="/L75/" 
            elif(IntensityData<=50 and IntensityData>25):
                intensity=50
                config="/L50/" 
            elif(IntensityData<=50 and IntensityData>0):
                intensity=25
                config="/L25/" 
            
            if(SpeedData<=100 and SpeedData>75):
                Speed=100 
                configFan="/M100/"            
            elif(SpeedData<=75 and SpeedData>50):
                Speed=75
                configFan="/M75/" 
            elif(SpeedData<=50 and SpeedData>25):
                Speed=50
                configFan="/M50/" 
            elif(SpeedData<=50 and SpeedData>0):
                Speed=25
                configFan="/M25/" 

            ip=self.lineEdit.text()        
            URL="http://"+ip+config
            try:
                r = requests.post(url = URL)
            except:
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Cooler Speed "+str(Speed))+"%")       
                x = msg.exec_()
            URL="http://"+ip+configFan
            try:
                r = requests.post(url = URL)
            except:
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Lights Brightness "+str(intensity))+"%")       
                x = msg.exec_()

        if(protocol=='Serial'):
            
            IntensityData=self.dial_2.value() 
            SpeedData=self.dial_3.value() 
            if(IntensityData<=100 and IntensityData>75):
                intensity=100   
                config="/L100/"         
            elif(IntensityData<=75 and IntensityData>50):
                intensity=75
                config="/L75/" 
            elif(IntensityData<=50 and IntensityData>25):
                intensity=50
                config="/L50/" 
            elif(IntensityData<=50 and IntensityData>0):
                intensity=25
                config="/L25/" 
            
            if(SpeedData<=100 and SpeedData>75):
                Speed=100 
                configFan="/M100/"            
            elif(SpeedData<=75 and SpeedData>50):
                Speed=75
                configFan="/M75/" 
            elif(SpeedData<=50 and SpeedData>25):
                Speed=50
                configFan="/M50/" 
            elif(SpeedData<=50 and SpeedData>0):
                Speed=25
                configFan="/M25/" 
            try:
                ser=PortFinder.FindPort()
                self.lineEdit.setText(ser)                    
                ser.write(str.encode(str(config))) 
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Lights Brightness "+str(intensity))+"%")       
                x = msg.exec_()
                time.sleep(1)
                ser.write(str.encode(str(configFan)))  
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT")
                msg.setText(str("MATTWARE Fan Speed "+str(Speed))+"%")       
                x = msg.exec_()
            except:
                self.lineEdit.setText("MATTWARE Not Connected") 
                
            
    def ADDUSER(self):
        import sqlite3
        username=str(self.lineEdit_3.text())
        email=str(self.lineEdit_4.text())
        os=str(self.comboBox_3.currentText())
        status=str(self.checkBox.isChecked())
        del_query="DELETE FROM USER"
        query="INSERT INTO USER( NAME, MAIL, OS, VOCAL_STATUS) VALUES (?,?,?,?);"
        conn = sqlite3.connect('DATABASE/MATTBOT2.db')  
        cursor = conn.cursor()
        cursor.execute(del_query)
        conn.commit() 
        cursor.execute(query,(username,email,os,status))
        conn.commit()       
        conn.close()
        mattUser=open("user.matt","w")
        data1=self.lineEdit_3.text()
        data2=self.lineEdit_4.text()
        mattUser.write(data1+",")
        mattUser.write(data2+",")
        mattUser.write(os+",")
        mattUser.write(status)
        mattUser.close()
        msg=QMessageBox()
        msg.setWindowTitle("MATTBot 🤖")
        msg.setText(str("ADDED NEW USER 🥳"))       
        x = msg.exec_()

    def REMOVE_ALL_REMINDERS(self):
        conn = sqlite3.connect('DATABASE/MATTBOT2.db')  
        cursor = conn.cursor()
        del_query="DELETE FROM REMINDERS;"
        cursor.execute(del_query)
        conn.commit() 
        self.listWidget.clear()
        msg=QMessageBox()
        msg.setWindowTitle("MATTBot 🤖")
        msg.setText(str("CLEARED ALL REMINDERS 🥳"))       
        x = msg.exec_()
        conn.close()

    def DELETE_REMINDER(self):
        datatobeDeleted=self.lineEdit_2.text()
        conn = sqlite3.connect('DATABASE/MATTBOT2.db')  
        cursor = conn.cursor()
        del_query="DELETE FROM REMINDERS WHERE (TOPIC=?);"
        cursor.execute(del_query,(datatobeDeleted,))
        conn.commit() 
        self.listWidget.clear()
        query="SELECT * from REMINDERS"        
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall();    
        #print(result)
        conn.close()
        listbro=[]
        listbro.clear()   
        for i in result:            
            a=str(i)[1:-1]
            listbro.append(a)  
        self.listWidget.clear()
        for i in listbro:            
            self.listWidget.addItem(i)
        listbro.clear()
        msg=QMessageBox()
        msg.setWindowTitle("MATTBot 🤖")
        msg.setText(str("CLEARED "+datatobeDeleted+" 🥳"))       
        x = msg.exec_()
        conn.close()

    def LANTALK(self):
        os.system('chat.pyw')

    def ADD_REMINDER(self):        
        import sqlite3
        reminder=self.lineEdit_2.text()
        time=self.timeEdit.text()
        date=self.dateEdit.text()
        query="INSERT INTO REMINDERS( TOPIC, TIME, DATE) VALUES (?,?,?);"
        conn = sqlite3.connect('DATABASE/MATTBOT2.db')  
        cursor = conn.cursor()
        cursor.execute(query,(reminder,time,date))
        conn.commit()   
        query="SELECT * from REMINDERS"        
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall();    
        #print(result)
        conn.close()
        listbro=[]
        listbro.clear()   
        for i in result:            
            a=str(i)[1:-1]
            listbro.append(a)  
        self.listWidget.clear()
        for i in listbro:            
            self.listWidget.addItem(i)
        listbro.clear()
        msg=QMessageBox()
        msg.setWindowTitle("MATTBot 🤖")
        msg.setText(str("ADDED NEW REMINDERS 🥳"))       
        x = msg.exec_()

    def displayTime(self):     
        #import SCHEDULER2   
        self.label_12.setText(QtCore.QDateTime.currentDateTime().time().toString())  
        reciever=self.comboBox.currentText()    
        if(reciever=="BOT"):   
            self.pushButton_15.setDisabled(True)  
            self.pushButton_5.setDisabled(True)      
            self.pushButton_14.setDisabled(True) 
            self.pushButton_6.setDisabled(False) 
            self.pushButton_12.setDisabled(False)
            self.pushButton_13.setDisabled(False)   
        if(reciever=="LAN"):   
            self.pushButton_15.setDisabled(False)  
            self.pushButton_5.setDisabled(True)      
            self.pushButton_14.setDisabled(True) 
            self.pushButton_6.setDisabled(True) 
            self.pushButton_12.setDisabled(True)
            self.pushButton_13.setDisabled(True)
        if(reciever=="-"):   
            self.pushButton_15.setDisabled(True)  
            self.pushButton_5.setDisabled(True)      
            self.pushButton_14.setDisabled(True) 
            self.pushButton_6.setDisabled(True) 
            self.pushButton_12.setDisabled(True)
            self.pushButton_13.setDisabled(True)
        DATE=self.dateEdit.text()
        current_time=str(self.label_12.text())
        TIME=current_time
        conn = sqlite3.connect('DATABASE/MATTBOT2.db')  
        cursor = conn.cursor()
        select_query="""SELECT TOPIC FROM REMINDERS WHERE TIME=? AND DATE=?;"""
        cursor.execute(select_query,(current_time,DATE))
        rows = cursor.fetchall()        
        for i in rows:
            msg=QMessageBox()
            msg.setWindowTitle("MATTBot 🤖")
            if(self.checkBox.isChecked()):
                HLEngine_audioProcess.readText(str(i)[1:-1])
            else:
                HLEngine_audioProcess.playsound(r"Reminders\reminder.mp3")
            protocol=self.comboBox_2.currentText()
            if(protocol=='BOOMER'):
                try:
                    port=str(self.lineEdit.text())
                    ser = serial.Serial(port, '9600')   
                    ser.write(str.encode("hi"))                 
                except:
                    print('BOOMER not connected ....')
                

            
            msg.setText(str("REMINDER:"+str(i)[1:-1]+"🤯"))       
            x = msg.exec_()

        

        if(TIME==timeMapper.nine):
            HLEngine_audioProcess.playsound("Reminders/9am.mp3")            
        elif(TIME==timeMapper.ten):
            HLEngine_audioProcess.playsound("Reminders/10am.mp3")
        elif(TIME==timeMapper.eleven):
            HLEngine_audioProcess.playsound("Reminders/11am.mp3")
        elif(TIME==timeMapper.twelve):
            HLEngine_audioProcess.playsound("Reminders/12pm.mp3")
        elif(TIME==timeMapper.thirteen):
            HLEngine_audioProcess.playsound("Reminders/1pm.mp3")
        elif(TIME==timeMapper.fourteen):
            HLEngine_audioProcess.playsound("Reminders/2pm.mp3")
        elif(TIME==timeMapper.fifteen):
            HLEngine_audioProcess.playsound("Reminders/3pm.mp3")
        elif(TIME==timeMapper.sixteen):
            HLEngine_audioProcess.playsound("Reminders/4pm.mp3")
        elif(TIME==timeMapper.seventeen):
            HLEngine_audioProcess.playsound("Reminders/5pm.mp3")
        elif(TIME==timeMapper.eighteen):
            HLEngine_audioProcess.playsound("Reminders/6pm.mp3")
        elif(TIME==timeMapper.nineteen):
            HLEngine_audioProcess.playsound("Reminders/7pm.mp3")
        elif(TIME==timeMapper.twenty):
            HLEngine_audioProcess.playsound("Reminders/8pm.mp3")
        elif(TIME==timeMapper.twentyone):
            HLEngine_audioProcess.playsound("Reminders/9pm.mp3")
        elif(TIME==timeMapper.twentytwo):
            HLEngine_audioProcess.playsound("Reminders/10pm.mp3")
        elif(TIME==timeMapper.twentythree):
            HLEngine_audioProcess.playsound("Reminders/11pm.mp3")
        elif(TIME==timeMapper.twentyfour):
            HLEngine_audioProcess.playsound("Reminders/12am.mp3")


        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MATTBot 2021.1"))
        self.label.setText(_translate("Dialog", "TIME"))
        self.label_2.setText(_translate("Dialog", "REMINDER"))
        self.pushButton_2.setText(_translate("Dialog", "Clear All"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "hh:mm:ss"))
        self.label_12.setText(_translate("Dialog", "loading..."))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_3.setText(_translate("Dialog", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Reminder"))
        self.label_5.setText(_translate("Dialog", "Message"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_5.setText(_translate("Dialog", "Refresh"))
        self.pushButton_6.setText(_translate("Dialog", "Send"))
        self.comboBox.setItemText(0, _translate("Dialog", "BOT"))
        self.comboBox.setItemText(1, _translate("Dialog", "LAN"))
        self.comboBox.setItemText(2, _translate("Dialog", "-"))
        #self.comboBox.setItemText(3, _translate("Dialog", "CLOUD"))
        self.pushButton_12.setText(_translate("Dialog", "Read Note"))
        self.pushButton_13.setText(_translate("Dialog", "Clear Note"))
        self.pushButton_14.setText(_translate("Dialog", "Poke"))
        self.pushButton_15.setText(_translate("Dialog", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Messenger"))
        self.label_8.setText(_translate("Dialog", "Speed"))
        self.label_9.setText(_translate("Dialog", "Light"))
        self.label_10.setText(_translate("Dialog", "0"))
        self.label_11.setText(_translate("Dialog", "0"))
        self.pushButton_7.setText(_translate("Dialog", "f(x)"))
        self.lineEdit.setText(_translate("Dialog", "MATTWare Address Here"))
        self.label_13.setText(_translate("Dialog", "*Protocol Address:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "IP"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "BOOMER"))
        self.pushButton_8.setText(_translate("Dialog", "FAN ON"))
        self.pushButton_9.setText(_translate("Dialog", "FAN OFF"))
        self.pushButton_10.setText(_translate("Dialog", "LIGHTS ON"))
        self.pushButton_11.setText(_translate("Dialog", "LIGHTS OFF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "MATTWare"))
        self.label_3.setText(_translate("Dialog", "*Name"))
        self.label_4.setText(_translate("Dialog", "*Email"))
        self.pushButton_4.setText(_translate("Dialog", "Save"))
        self.checkBox.setText(_translate("Dialog", "Enable Vocal Content Alert"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Select OS"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Windows OS"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Linux OS"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "MAC OS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Settings"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">Freeware Developed by:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">HL Robotics &amp;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Software Automation 2021</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">www.hlengine.tech</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">akhil.pj007@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Address:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Puthupparampil House</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Manjadi P.O Thiruvalla 689105</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MATTBOT()
    ui.mattbot(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
