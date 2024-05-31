# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
from random import randint, randrange
from PyQt5 import QtCore, QtGui, QtWidgets


class SignUp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 594)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    background-image: url(../images.qrc/home-hero-left.webp);\n"
"    \n"
"background-repeat:no-repeat;\n"
"};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bgwidget)
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.bgwidget)
        self.frame.setStyleSheet("QFrame#frame\n"
"{\n"
"    background-color:#013220;\n"
"border-radius: 10px;\n"
"};")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(400, 10, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:25px;\n"
"color:beige;")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.M_Name = QtWidgets.QLineEdit(self.frame)
        self.M_Name.setGeometry(QtCore.QRect(170, 170, 311, 31))
        self.M_Name.setStyleSheet("border:none;\n color:beige"
"border-bottom:1px solid black;")
        self.M_Name.setObjectName("M_Name")

        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(540, 140, 121, 16))
        self.label_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(540, 180, 121, 16))
        self.label_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 220, 121, 16))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_8.setObjectName("label_8")
        self.user_name = QtWidgets.QLineEdit(self.frame)
        self.user_name.setGeometry(QtCore.QRect(170, 290, 311, 31))
        self.user_name.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")

        self.user_name.setPlaceholderText("")
        self.user_name.setObjectName("user_name")
        self.H_No = QtWidgets.QLineEdit(self.frame)
        self.H_No.setGeometry(QtCore.QRect(670, 130, 311, 31))
        self.H_No.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")
        self.H_No.setObjectName("H_No")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(35, 340, 121, 16))
        self.label_15.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 260, 121, 16))
        self.label_13.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_13.setObjectName("label_13")
        self.F_Name = QtWidgets.QLineEdit(self.frame)
        self.F_Name.setGeometry(QtCore.QRect(170, 130, 311, 31))
        self.F_Name.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")
        self.F_Name.setObjectName("F_Name")

        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(40, 300, 121, 16))
        self.label_14.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_14.setObjectName("label_14")



        self.Street_No = QtWidgets.QLineEdit(self.frame)
        self.Street_No.setGeometry(QtCore.QRect(670, 170, 311, 31))
        self.Street_No.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")
        self.Street_No.setText("")
        self.Street_No.setObjectName("Street_No")



        self.L_Name = QtWidgets.QLineEdit(self.frame)
        self.L_Name.setGeometry(QtCore.QRect(170, 210, 311, 31))
        self.L_Name.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")
        self.L_Name.setText("")
        self.L_Name.setObjectName("L_Name")

        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(540, 220, 121, 16))
        self.label_11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_11.setObjectName("label_11")

        self.Passwrd = QtWidgets.QLineEdit(self.frame)
        self.Passwrd.setGeometry(QtCore.QRect(170, 330, 311, 31))
        self.Passwrd.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")
        self.Passwrd.setObjectName("Passwrd")
        self.U_Division = QtWidgets.QLineEdit(self.frame)
        self.U_Division.setGeometry(QtCore.QRect(670, 210, 311, 31))
        self.U_Division.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")
        self.U_Division.setObjectName("U_Division")
        self.MeterNo = QtWidgets.QLineEdit(self.frame)
        self.MeterNo.setGeometry(QtCore.QRect(170, 250, 311, 31))
        self.MeterNo.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;")
        self.MeterNo.setObjectName("MeterNo")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 180, 121, 16))
        self.label_12.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_12.setObjectName("label_12")

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.clicked.connect(lambda: self.takingValue())
        self.pushButton_6.setGeometry(QtCore.QRect(420, 450, 261, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color:rgb(30,144,255);\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(30,144,255);\n"
"border:1px solid rgb(30,144,255);\n"
"transform:scale(1.2);\n"
"\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(320, 70, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(300, 400, 601, 16))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.bgwidget)
        self.checkBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
                                    "")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", " ⓔ PMS"))
        self.M_Name.setPlaceholderText(_translate("Dialog", "e.g. Musa"))

        self.label_9.setText(_translate("Dialog", "Address"))
        self.label_10.setText(_translate("Dialog", "City"))
        self.label_8.setText(_translate("Dialog", "Last Name"))
        self.H_No.setPlaceholderText(_translate("Dialog", "Enter your Address"))
        self.label_15.setText(_translate("Dialog", " Confirm Password"))
        self.label_13.setText(_translate("Dialog", "Username "))
        self.F_Name.setPlaceholderText(_translate("Dialog", "e.g. Sara"))

        self.label_14.setText(_translate("Dialog", "Password"))
        self.user_name.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.Street_No.setPlaceholderText(_translate("Dialog", "Enter your City"))
        self.L_Name.setPlaceholderText(_translate("Dialog", "e.g. Arshad"))


        self.label_11.setText(_translate("Dialog", "Division"))

        self.Passwrd.setPlaceholderText(_translate("Dialog", "Enter Your Password"))
        self.U_Division.setPlaceholderText(_translate("Dialog", "Enter your Division "))
        self.MeterNo.setPlaceholderText(_translate("Dialog", "Enter username"))
        self.label_7.setText(_translate("Dialog", "First Name"))
        self.label_12.setText(_translate("Dialog", "Middle Name"))

        self.pushButton_6.setText(_translate("Dialog", "Sign Me Up"))
        self.label.setText(_translate("Dialog", ""))
        self.checkBox.setText(_translate("Dialog", "Agree Privacy Policy and our Terms and Conditions."))

    def takingValue(self):
        msg = QMessageBox()
        if self.F_Name.text() == "" or self.MeterNo.text() == "" or self.Passwrd.text() == "" or self.checkBox.isChecked() == False:
            msg.setText("Fill All Required Fields")
            msg.setWindowTitle("Error")
            w = msg.exec_()
        else:
            try:
                User_name = self.MeterNo.text()
                F_Name = self.F_Name.text()
                M_Name = self.M_Name.text()
                L_Name = self.L_Name.text()
                Password = self.Passwrd.text()
                con_Passwrd = self.user_name.text()
                address = self.H_No.text()
                City = self.Street_No.text()
                division=self.U_Division.text()


                with cx_Oracle.connect('system/Oracle_1') as co:
                    cur = co.cursor()
                    sql0 = """INSERT INTO PERSON_T10 VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9)"""

                    cur.execute(sql0, [F_Name, M_Name, L_Name,   User_name, Password, con_Passwrd, address, City,  division])


                    co.commit()
                msg = QMessageBox()
                msg.setText("Congratualtions! You have signup successfully ")
                msg.setWindowTitle("Success")
                msg.exec_()
            except Exception as e:
                print("Error: ", str(e))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = SignUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
