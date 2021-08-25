'''
Developed by:Akhil P Jacob
HLRobotics and Software Automation 2021
'''


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import time
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_wiki
import requests
from FireStorage import FirePlay
from Seeker import timeMapper
global Reminders
global Recurring_Reminders
Recurring_Reminders=[]
dataViewer=[]
config=open('user.matt','r')
USER=config.read()
USER=USER.split(",")
config.close()
datefile=open('date.matt','r')
data=datefile.read()
Dates=data.split(" ")
Dates.remove("")
datefile.close()
reminderfile=open('reminders.matt','r')
data=reminderfile.read()
Reminders=data.split(" ")
Reminders.remove("")
reminderfile.close()
HLEngine_audioProcess.playAudio("Reminders\Welcome.mp3")

class MATTBOTv2(object):
    def mattbotv2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 270)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Design/MattBot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 251))
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
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(10, 90, 461, 121))
        self.listView.setStyleSheet("color: rgb(164, 0, 0);")
        self.listView.setObjectName("listView")
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 20, 241, 25))
        self.lineEdit_5.setStyleSheet("color: rgb(52, 101, 164);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 341, 131))
        self.textEdit.setStyleSheet("color: rgb(204, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 90, 111, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 60, 111, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(360, 20, 111, 25))
        self.comboBox.setStyleSheet("color: rgb(32, 74, 135);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.lineEdit.setGeometry(QtCore.QRect(160, 180, 161, 25))
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
        self.textBrowser.setGeometry(QtCore.QRect(210, 10, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 191, 191))
        self.label_7.setStyleSheet("border-image: url(Design/MattBot.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_3, "")

        


        self.timer = QtCore.QTimer(Dialog)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        self.dial_2.setMaximum(100)
        self.dial_2.setMinimum(0)
        self.dial_2.setValue(100)
        self.dial_2.valueChanged.connect(self.lightAnalog)

        self.dial_3.setMaximum(100)
        self.dial_3.setMinimum(0)
        self.dial_3.setValue(100)
        self.dial_3.valueChanged.connect(self.fanAnalog)

        self.pushButton.clicked.connect(self.saveTime)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_6.clicked.connect(self.Message_Sent)
        self.pushButton_5.clicked.connect(self.GetMessage)
        self.pushButton_4.clicked.connect(self.save_USER)
        #self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_8.clicked.connect(self.fanON)
        self.pushButton_9.clicked.connect(self.fanOFF)
        self.pushButton_10.clicked.connect(self.lightsON)
        self.pushButton_11.clicked.connect(self.lightsOFF)
        self.pushButton_7.clicked.connect(self.Send)
        self.dateEdit.setDate(QDate.currentDate())
        #try:
        self.lineEdit_3.setText(USER[0])
        self.lineEdit_4.setText(USER[1])
        status=USER[2]
        if(status=="True"):
            self.checkBox.setChecked(1)
        OS=USER[3]
        if(OS=="Windows OS"):
            self.comboBox_3.setCurrentIndex(1) 
        if(OS=="Linux OS"):
            self.comboBox_3.setCurrentIndex(2)   
        if(OS=="MAC OS"):
            self.comboBox_3.setCurrentIndex(3)    
        if(OS=="Select OS"):
            self.comboBox_3.setCurrentIndex(0) 

        
        
        #except:
        #    self.lineEdit_3.setText("Enter your NAME")
        #    self.lineEdit_4.setText("Enter your mail ID")
        

        model=QtGui.QStandardItemModel()
        self.listView.setModel(model)
        global b1
        global a1
        a1=0
        b1=0
        a="0"
        b="0"
        for i in Reminders:
                if(Reminders.index(i)%2==0):
                        a=str(i)       
                if(Reminders.index(i)%2!=0):
                        b=str(i)
        
                if(a!="0" and b!="0" and b!=b1 and a1!=a):
                        val=a+"-->"+b
                        if(val in dataViewer):
                                a="0"
                                b="0"                                
                                pass
                        else:
                                b1=b
                                a1=a
                                dataViewer.append(val)
        for i in dataViewer:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MATTBot 2021 ver 2.0"))
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
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>"))
        self.pushButton_5.setText(_translate("Dialog", "Refresh"))
        self.pushButton_6.setText(_translate("Dialog", "Send"))
        self.comboBox.setItemText(0, _translate("Dialog", "BOT"))
        self.comboBox.setItemText(1, _translate("Dialog", "LAN"))
        self.comboBox.setItemText(2, _translate("Dialog", "UNITY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Messenger"))
        self.label_8.setText(_translate("Dialog", "Speed"))
        self.label_9.setText(_translate("Dialog", "Light"))
        self.label_10.setText(_translate("Dialog", "0"))
        self.label_11.setText(_translate("Dialog", "0"))
        self.pushButton_7.setText(_translate("Dialog", "f(x)"))
        self.lineEdit.setText(_translate("Dialog", "MATTWare Address Here"))
        self.label_13.setText(_translate("Dialog", "*Protocol Address:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "IP"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Serial"))
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
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Freeware Developed by:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">HL Robotics &amp;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Software Automation 2021</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">www.hlengine.tech</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">akhil.pj007@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Address:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Puthupparampil House</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Manjadi P.O Thiruvalla 689105</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "About"))


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

        

    def save_USER(self):        
        mattUser=open("user.matt","w")
        data1=self.lineEdit_3.text()
        data2=self.lineEdit_4.text()
        status=self.checkBox.isChecked()
        os=self.comboBox_3.currentText()
        mattUser.write(data1+",")
        mattUser.write(data2+",")
        mattUser.write(str(status)+",")
        mattUser.write(os)
        mattUser.close()
        msg=QMessageBox()
        msg.setWindowTitle("MATTBOT")
        msg.setText(str("Added User Configurations"))       
        x = msg.exec_()
       

    def update(self):
        try:
            import git
            import cv2
            import subprocess
            import sys     
            self.progressBar.setProperty("value", 25)   
            
            git_dir = "../MATTBot_2021/"
            g = git.cmd.Git(git_dir)
            g.pull()
            self.progressBar.setProperty("value", 70)
            self.label_6.setText("*Updated Successfully, Please Restart MATTBOT APRICOT")
            self.progressBar.setProperty("value", 100)
            msg=QMessageBox()
            msg.setWindowTitle("MATTBOT")
            msg.setText(str("Updated Successfully !!!"))       
            x = msg.exec_()
        except:
            msg=QMessageBox()
            msg.setWindowTitle("MATTBOT")
            msg.setText(str("Updates Denied !!!"))       
            x = msg.exec_()
            self.label_6.setText("*Failed to Update MATTBOT APRICOT")
            self.progressBar.setProperty("value", 0)
      
    def saveTime(self):

        currentTime=self.timeEdit.text()
        currentTime=currentTime
        currentDate=self.dateEdit.text()        
        content_Reminder=self.lineEdit_2.text()        
        if(currentTime in Reminders):
            pass
        else:
            Reminders.append(currentTime)
            Reminders.append(content_Reminder)  
            Dates.append(currentDate)    
        reminder_file=open('reminders.matt','w')  
        for i in Reminders:            
            reminder_file.write(i)
            reminder_file.write(" ")
        reminder_file.close()
        date_file=open('date.matt','w')
        for i in Dates:
            date_file.write(i)
            date_file.write(" ")
        date_file.close()
        model=QtGui.QStandardItemModel()
        self.listView.setModel(model)
        
        global b1
        global a1
        a1=0
        b1=0
        a="0"
        b="0"
        for i in Reminders:
                if(Reminders.index(i)%2==0):
                        a=str(i)       
                if(Reminders.index(i)%2!=0):
                        b=str(i)
        
                if(a!="0" and b!="0" and b!=b1 and a1!=a):
                        val=a+"-->"+b
                        if(val in dataViewer):
                                a="0"
                                b="0"                                
                                pass
                        else:
                                b1=b
                                a1=a
                                dataViewer.append(val)
        for i in dataViewer:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)

    def recurringReminders(self):
        currentTime=self.timeEdit.text()        
        content_Reminder=self.lineEdit_2.text()
        Recurring_Reminders.append(currentTime)
        Recurring_Reminders.append(content_Reminder)
        Reminders.append(currentTime)
        Reminders.append(content_Reminder)
        model=QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in Reminders:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def clear(self):
        reminder_file=open('reminders.matt','w')
        reminder_file.close()
        date_file=open('date.matt','w')
        date_file.close()
        Reminders.clear()
        Recurring_Reminders.clear()
        Dates.clear()
        dataViewer.clear()
        model=QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in Reminders:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        msg=QMessageBox()
        msg.setWindowTitle("MATTBOT")
        msg.setText(str("Reminders Cleared"))       
        x = msg.exec_()

    def Message_Sent(self):      
        reciever=self.comboBox.currentText()    
        if(reciever=="Bot"):   
            query=self.lineEdit_5.text()
            response=HLEngine_wiki.wiki(query)
            self.textEdit.setText(response)
            
        elif(reciever=="Unity"):
            User=self.lineEdit_3.text()  
            Message=self.lineEdit_5.text()
            status=FirePlay.FireData_SEND(User, Message)     
            if(status==True):
                self.textEdit.setText("[Message delivered]")

    
    def GetMessage(self):
        reciever=self.comboBox.currentText()    
        if(reciever=="Bot"):   
            self.textEdit.setText("[Still on Development]")
        elif(reciever=="Unity"):
            message=FirePlay.FireData_RECIEVE()
            print(message)
            self.textEdit.setText(str(message))
            

    def displayTime(self):
        TimeHits=[]        
        ReminderHits=[]
        TimeHits2=[]
        ReminderHits2=[]
        protocol=self.comboBox_2.currentText()
        OS=USER[3]
        #print(protocol)
        if(protocol=="IP"):
            self.lineEdit.setText("192.168.x.x")
        if(protocol=="Serial" and OS=="Windows OS"):
            self.lineEdit.setText("COMx")
        if(protocol=="Serial" and OS=="Linux OS"):
            self.lineEdit.setText("/dev/ttyUSB0")
        if(protocol=="Serial" and OS=="MAC OS"):
            self.lineEdit.setText("/dev/ttyUSB0")
        if(protocol=="Serial" and OS=="Select OS"):
            self.lineEdit.setText("COM PORT")
        
        
        self.label_12.setText(QtCore.QDateTime.currentDateTime().time().toString())
        TIME=self.label_12.text() 
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

       
        for i in Reminders:
            index=Reminders.index(i)
            if(index%2!=0):
                ReminderHits.append(i)
            elif(index%2==0):
                TimeHits.append(i)
        '''
        for i in Recurring_Reminders:
            index=Recurring_Reminders.index(i)
            if(index%2!=0):
                ReminderHits2.append(i)
            elif(index%2==0):
                TimeHits2.append(i)
        '''
        
              
        if (TIME  in TimeHits):           
            reminderIndex=TimeHits.index(TIME)
            reminderData=ReminderHits[reminderIndex]
            date=str(Dates[reminderIndex])   
                
            if(date==self.dateEdit.text()):
                msg=QMessageBox()
                msg.setWindowTitle("MATTBOT REMINDER")
                msg.setText(str(reminderData))
                HLEngine_audioProcess.playsound("Reminders/reminder.mp3")
                x = msg.exec_()

        if (TIME  in TimeHits2):
            reminderIndex=TimeHits2.index(TIME)
            reminderData=ReminderHits2[reminderIndex]
            msg=QMessageBox()
            msg.setWindowTitle("MATTBOT YOUR HEALTH REMINDER")
            msg.setText(str(reminderData))
            HLEngine_audioProcess.playsound("Reminders/water.mp3")
            x = msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MATTBOTv2()
    ui.mattbotv2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
