import sqlite3


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.listWidget.setObjectName("listWidget")


        conn = sqlite3.connect('DATABASE/MATTBOT2.db')  
        cursor = conn.cursor()        
        query="SELECT * from REMINDERS"        
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall();    
        conn.close()
        listbro=[]
        for i in result:
            a=str(i)[1:-1]
            #print(a)
            listbro.append(a)
        print(listbro)
        for i in listbro:
            self.listWidget.addItem(i)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LIST WINDOW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
