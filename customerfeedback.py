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
from random import randint, randrange
import cx_Oracle
from PyQt5 import QtCore, QtGui, QtWidgets


class FB(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 671)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    \n"
"    background-image: url(:/newPrefix/Desktop/images.qrc/home-hero-left.webp);\n"
"background-repeat:no-repeat;\n"
"};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bgwidget)
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.bgwidget)
        self.groupBox.setStyleSheet("QGroupBox#groupBox\n"
"{\n"
"background-color:#013220;\n"
"border-radius:10px;\n"
"};")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(510, 120, 441, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../garbage/FeedbackImage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.Fdbck_Name = QtWidgets.QLineEdit(self.groupBox)
        self.Fdbck_Name.setGeometry(QtCore.QRect(160, 240, 291, 31))
        self.Fdbck_Name.setObjectName("Fdbck_Name")

        self.F_Department = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department.setGeometry(QtCore.QRect(160, 200, 291, 31))
        self.F_Department.setObjectName("F_Department")

        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(50, 290, 121, 16))
        self.label_33.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_33.setObjectName("label_33")


        self.F_Department_2 = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department_2.setGeometry(QtCore.QRect(160, 200, 291, 31))
        self.F_Department_2.setStyleSheet("border:none;color:beige\n"
"border-bottom:1px solid black;;color:beige\n"
"")
        self.F_Department_2.setObjectName("F_Department_2")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(50, 290, 121, 16))
        self.label_34.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";;color:beige\n"
"")
        self.label_34.setObjectName("label_34")
        self.Fdbck_Desc_2 = QtWidgets.QTextEdit(self.groupBox)
        self.Fdbck_Desc_2.setGeometry(QtCore.QRect(160, 280, 291, 79))
        self.Fdbck_Desc_2.setStyleSheet("border:none;;color:beige\n"
"border-bottom:1px solid black;;color:beige\n"
"")
        self.Fdbck_Desc_2.setObjectName("Fdbck_Desc_2")
        self.SubmitFdbckBtn_2 = QtWidgets.QPushButton(self.groupBox)
        self.SubmitFdbckBtn_2.setGeometry(QtCore.QRect(130, 440, 271, 41))
        self.SubmitFdbckBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitFdbckBtn_2.setStyleSheet("QPushButton{\n"
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
        self.SubmitFdbckBtn_2.clicked.connect(lambda : self.valueEntry())
        self.SubmitFdbckBtn_2.setObjectName("SubmitFdbckBtn_2")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setGeometry(QtCore.QRect(50, 250, 121, 16))
        self.label_35.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox)
        self.label_36.setGeometry(QtCore.QRect(50, 210, 101, 20))
        self.label_36.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_36.setObjectName("label_36")
        self.Fdbck_Name_2 = QtWidgets.QLineEdit(self.groupBox)
        self.Fdbck_Name_2.setGeometry(QtCore.QRect(160, 240, 291, 31))
        self.Fdbck_Name_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"")
        self.Fdbck_Name_2.setObjectName("Fdbck_Name_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(470, 10, 521, 600))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/Desktop/images.qrc/FeedbackImage.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:/downloads/question-mark-1872665_640.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 381, 51))
        self.label_3.setStyleSheet("font: 80 15pt \"MS Shell Dlg 2\";color:beige;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(840, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setStyleSheet("color:beige;")
        self.label_4.setObjectName("label_4")
        self.F_Department_3 = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department_3.setGeometry(QtCore.QRect(160, 160, 291, 31))
        self.F_Department_3.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;;color:black\n"
"")
        self.F_Department_3.setObjectName("F_Department_3")
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(50, 170, 101, 20))
        self.label_37.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";;color:beige\n"
"")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


        self.F_Department.setPlaceholderText(_translate("Dialog", "Department"))

        self.label_33.setText(_translate("Dialog", "Description"))

        self.F_Department_2.setPlaceholderText(_translate("Dialog", "Enter your First Name"))

        self.Fdbck_Desc_2.setPlaceholderText(_translate("Dialog", "Enter Description"))
        self.SubmitFdbckBtn_2.setText(_translate("Dialog", "Send Feedback"))
        self.label_35.setText(_translate("Dialog", " Last  Name"))
        self.label_36.setText(_translate("Dialog", "First Name"))
        self.Fdbck_Name_2.setPlaceholderText(_translate("Dialog", "Enter your Last Name"))
        self.label_3.setText(_translate("Dialog", "Your Feedback Matters The Most!"))
        self.label_4.setText(_translate("Dialog", "ⓔ PMS"))
        self.F_Department_3.setPlaceholderText(_translate("Dialog", "Enter your CNIC no."))
        self.label_37.setText(_translate("Dialog", "CNIC no. "))


    def valueEntry(self):
             msg = QMessageBox()
             if self.F_Department_2.text() == "" or self.Fdbck_Name_2.text() == "" or self.Fdbck_Desc_2.text() == "" or self.F_Department_3.text()== "":
                 msg.setText("Fill All Required Fields")
                 msg.setWindowTitle("Error")
                 w = msg.exec_()

             else:
                First_name = self.F_Department_2.text()
                Last_name = self.Fdbck_Name_2.text()
                description = self.Fdbck_Desc_2.text()
                CNIC_no = int(self.F_Department_3.text())



                try:
                    with cx_Oracle.connect('system/Oracle_1') as co:
                         cur = co.cursor()

                         sql_6 = """INSERT INTO FEED_BACK( First_name, Last_name, description, CNIC_no) 
                                       VALUES (:1, :2, :3, :4)"""
                         cur.execute(sql_6, [First_name, Last_name, description,CNIC_no])

                         co.commit()
                         msg = QMessageBox()
                         msg.setText("Feedback is submitted Successfully")
                         msg.setWindowTitle("Success")
                         w = msg.exec_()

                except cx_Oracle.Error as error:
                    print("Error:", error)
                    msg.setText("Error in submitting feedback. Please try again.")
                    msg.setWindowTitle("Error")
                    w = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = FB()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())









