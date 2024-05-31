from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from datetime import date
from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint, randrange
import cx_Oracle


class Trans(object):
    def window(self):
        self.window = QtWidgets.QDialog()

        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 554)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 5000, 0, 1000))
        self.bgwidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bgwidget.setStyleSheet("QWidget#bgwidget\n"
"{\n"
"background-image: url();\n"
"background-repeat:no-repeat;\n"
"background-size: cover;\n"                                    
"};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.groupBox = QtWidgets.QGroupBox(self.bgwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 40, 931, 441))
        self.groupBox.setStyleSheet("QGroupBox#groupBox\n"
"{\n"
"border-radius:10px;\n"
"background-color:#013220;\n"
"};\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.label_2.setStyleSheet("background-image: url(E:/downloads/side-view-valet-doing-his-job.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:/downloads/side-view-valet-doing-his-job.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(560, 20, 311, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 80 15pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_7.setObjectName("label_7")
        self.CardPin_2 = QtWidgets.QLineEdit(self.groupBox)
        self.CardPin_2.setGeometry(QtCore.QRect(570, 230, 311, 31))
        self.CardPin_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.CardPin_2.setText("")
        self.CardPin_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CardPin_2.setObjectName("CardPin_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(550, 120, 151, 16))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_5.setObjectName("label_5")
        self.ATMCardNo_2 = QtWidgets.QLineEdit(self.groupBox)
        self.ATMCardNo_2.setGeometry(QtCore.QRect(570, 150, 311, 31))
        self.ATMCardNo_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.ATMCardNo_2.setObjectName("ATMCardNo_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(550, 200, 121, 16))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_6.setObjectName("label_6")
        self.MakeTransaction_2 = QtWidgets.QPushButton(self.groupBox)
        self.MakeTransaction_2.clicked.connect(lambda : self.cred_value())
        self.MakeTransaction_2.setGeometry(QtCore.QRect(620, 370, 221, 41))
        self.MakeTransaction_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(30,144,255);\n"
"color:white;\n"
"border-radius:20px;\n"
"font-size:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(30,144,255);\n"
"border:1px solid rgb(30,144,255);\n"
"transform:scale(1.2);\n"
"}")
        self.MakeTransaction_2.setObjectName("MakeTransaction_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:beige;")
        self.label.setObjectName("label")
        self.CardPin_3 = QtWidgets.QLineEdit(self.groupBox)
        self.CardPin_3.setGeometry(QtCore.QRect(570, 310, 311, 31))
        self.CardPin_3.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.CardPin_3.setText("")
        self.CardPin_3.setObjectName("CardPin_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(550, 280, 121, 16))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "Make Your Transactions Online!"))
        self.CardPin_2.setPlaceholderText(_translate("Dialog", "Pin"))
        self.label_5.setText(_translate("Dialog", "ATM Card No"))
        self.ATMCardNo_2.setPlaceholderText(_translate("Dialog", "Card No"))
        self.label_6.setText(_translate("Dialog", "Card Pin"))
        self.MakeTransaction_2.setText(_translate("Dialog", "Make Transaction"))
        self.label.setText(_translate("Dialog", "ⓔ PMS"))
        self.CardPin_3.setPlaceholderText(_translate("Dialog", "Enter your CNIC"))
        self.label_8.setText(_translate("Dialog", "CNIC no."))




    def cred_value(self):
                    msg = QMessageBox()
                    if self.CardPin_3.text() == "" or self.ATMCardNo_2.text() == "" or self.CardPin_2.text() == "":
                        msg.setText("Fill All Required Fields")
                        msg.setWindowTitle("Error")
                        w = msg.exec_()
                    else:
                        Atm_pin = int(self.CardPin_2.text())
                        Atm_card = self.ATMCardNo_2.text()
                        CNIC_no = self.CardPin_3.text()

                        try:
                            with cx_Oracle.connect('system/Oracle_1') as co:
                                cur = co.cursor()

                                # Insert into TRANS_FEE table with CNIC as a foreign key
                                sql_insert = """INSERT INTO TRANS_FEE_PASS (Atm_pin, Atm_card, CNIC_no) 
                                                VALUES (:1, :2, :3)"""
                                cur.execute(sql_insert, [Atm_pin, Atm_card, CNIC_no])

                                co.commit()
                                msg = QMessageBox()
                                msg.setText("Transaction Successful")
                                msg.setWindowTitle("Success")
                                w = msg.exec_()

                        except cx_Oracle.Error as error:
                            print("Error:", error)
                            msg = QMessageBox()
                            msg.setText("Error in transaction. Please try again.")
                            msg.setWindowTitle("Error")
                            w = msg.exec_()

                # Note: Replace 'YourClassName' with the actual name of your class.





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Trans()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
