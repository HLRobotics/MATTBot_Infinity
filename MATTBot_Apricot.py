import time
from HLEngine import HLEngine_audioProcess
from Seeker import timeMapper,user
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
global Reminders
Reminders=[]
global Recurring_Reminders
Recurring_Reminders=[]
config=open('user.matt','r')
USER=config.read()
USER=USER.split(",")
config.close()
from PyQt5 import QtCore, QtGui, QtWidgets


class Apricot(object):
    def apricot(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Design/HLD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(240, 10, 201, 16))
        self.label_12.setStyleSheet("color: rgb(204, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 60, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab, "")
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
        Dialog.setWindowTitle(_translate("Dialog", "MATTBOT Apricot"))
        self.label.setText(_translate("Dialog", "TIME"))
        self.label_2.setText(_translate("Dialog", "REMINDER"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Health"))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "hh:mm:ss"))
        self.label_12.setText(_translate("Dialog", "Loading..."))
        self.pushButton_5.setText(_translate("Dialog", "Clear All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Reminder"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">MATTBot Apricot 2021</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Built By</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HLRobotics &amp; Software Automation 2021</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">HLEngine Development Package</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visit:www.hlengine.tech</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "About"))

        self.timer = QtCore.QTimer(Dialog)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        self.pushButton.clicked.connect(self.saveTime)
        self.pushButton_2.clicked.connect(self.recurringReminders)
        self.pushButton_5.clicked.connect(self.clear_all)
    
    def clear_all(self):
        msg=QMessageBox()
        msg.setWindowTitle("MATTBOT Apricot")
        msg.setText(str("Cleared All Entries"))
        model=QtGui.QStandardItemModel()
        Reminders.clear()
        Recurring_Reminders.clear()
        self.listView.setModel(model)
        for i in Reminders:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def saveTime(self):
        currentTime=self.timeEdit.text()
        currentTime=currentTime
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
            msg.setWindowTitle("IMPORTANT")
            msg.setText(str(reminderData))
            HLEngine_audioProcess.playsound("Reminders/reminder.mp3")
            x = msg.exec_()

        if (TIME  in TimeHits2):
            reminderIndex=TimeHits2.index(TIME)
            reminderData=ReminderHits2[reminderIndex]
            msg=QMessageBox()
            msg.setWindowTitle("IMPORTANT")
            msg.setText(str(reminderData))
            HLEngine_audioProcess.playsound("Reminders/water.mp3")
            x = msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Apricot()
    ui.apricot(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
