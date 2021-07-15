
import time
from HLEngine import HLEngine_audioProcess
from Seeker import timeMapper
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
global Reminders
Reminders=[]
global Recurring_Reminders
Recurring_Reminders=[]

class MATTBOT2(object):
    def mattbot2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Design/MattBot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 151, 17))
        self.label_2.setStyleSheet("color: rgb(52, 101, 164);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 30, 331, 25))
        self.lineEdit_2.setStyleSheet("color: rgb(164, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 111, 25))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(10, 90, 461, 121))
        self.listView.setStyleSheet("color: rgb(164, 0, 0);")
        self.listView.setObjectName("listView")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 60, 111, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab)
        self.timeEdit.setGeometry(QtCore.QRect(10, 30, 118, 26))
        self.timeEdit.setObjectName("timeEdit")
        #self.timeEdit.setTimeRange(QTimeEdit(3, 00, 00), QTimeEdit(23, 30, 00))
        #self.timeEdit.setDisplayFormat('hh:mm:ss')
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(270, 60, 201, 16))
        self.label_12.setStyleSheet("color: rgb(204, 0, 0);")
        self.label_12.setObjectName("label_12")
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
        self.comboBox.setObjectName("comboBox")
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
        self.lineEdit.setGeometry(QtCore.QRect(40, 180, 161, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.dial_3 = QtWidgets.QDial(self.tab_5)
        self.dial_3.setGeometry(QtCore.QRect(200, 40, 171, 121))
        self.dial_3.setObjectName("dial_3")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(10, 180, 31, 17))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 120, 351, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar.setGeometry(QtCore.QRect(10, 160, 451, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 90, 351, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 411, 17))
        self.label_6.setObjectName("label_6")
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

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MATTBot 2021"))
        self.label.setText(_translate("Dialog", "TIME"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "hh:mm:ss"))
        self.label_2.setText(_translate("Dialog", "REMINDER"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Health"))
        self.label_12.setText(_translate("Dialog", "loading..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Reminder"))
        self.label_5.setText(_translate("Dialog", "Message"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_5.setText(_translate("Dialog", "Refresh"))
        self.pushButton_6.setText(_translate("Dialog", "Send"))
        self.comboBox.setItemText(0, _translate("Dialog", "Bot"))
        self.comboBox.setItemText(1, _translate("Dialog", "Unity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Messenger"))
        self.label_8.setText(_translate("Dialog", "Speed"))
        self.label_9.setText(_translate("Dialog", "Light"))
        self.label_10.setText(_translate("Dialog", "0"))
        self.label_11.setText(_translate("Dialog", "0"))
        self.pushButton_7.setText(_translate("Dialog", "Security"))
        self.lineEdit.setText(_translate("Dialog", "192.168.1.20"))
        self.label_13.setText(_translate("Dialog", "IP:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "IP"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Serial"))
        self.pushButton_8.setText(_translate("Dialog", "Fan ON"))
        self.pushButton_9.setText(_translate("Dialog", "Fan OFF"))
        self.pushButton_10.setText(_translate("Dialog", "Light ON"))
        self.pushButton_11.setText(_translate("Dialog", "LIGHTS OFF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "MATTWare"))
        self.label_3.setText(_translate("Dialog", "*Name"))
        self.label_4.setText(_translate("Dialog", "*Email"))
        self.pushButton_3.setText(_translate("Dialog", "Check for Updates"))
        self.pushButton_4.setText(_translate("Dialog", "Save"))
        self.label_6.setText(_translate("Dialog", "*update will be reflected after restarting MATTBot 2021"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Settings"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HL Dynamic Integration Technologies 2021</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hlroboticsautomation@gmail.com</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Last updated: 15th July 2021</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "About"))

        self.timer = QtCore.QTimer(Dialog)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        self.pushButton.clicked.connect(self.saveTime)
        self.pushButton_2.clicked.connect(self.recurringReminders)

    


    def saveTime(self):
        currentTime=self.timeEdit.text()
        currentTime=currentTime+":00"
        content_Reminder=self.lineEdit_2.text()
        Reminders.append(currentTime)
        Reminders.append(content_Reminder)
        model=QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in Reminders:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def recurringReminders(self):
        currentTime=self.timeEdit.text()
        currentTime=currentTime+":00"
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

        

    def displayTime(self):
        TimeHits=[]
        ReminderHits=[]
        TimeHits2=[]
        ReminderHits2=[]

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

        for i in Recurring_Reminders:
            index=Recurring_Reminders.index(i)
            if(index%2!=0):
                ReminderHits2.append(i)
            elif(index%2==0):
                TimeHits2.append(i)
              
        if (TIME  in TimeHits):
            reminderIndex=TimeHits.index(TIME)
            reminderData=ReminderHits[reminderIndex]
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
    ui = MATTBOT2()
    ui.mattbot2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
