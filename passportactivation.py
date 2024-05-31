from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from datetime import date
from random import randint, randrange
import cx_Oracle

class pass_acti(object):

    def openWindow(self):
        exit()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 594)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    background-image:  url(../images.qrc/vecteezy_hexagon-abstract-modern-background-with-overlapping-triangle_5909540.jpg);\n"
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
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family:\'Montserrat\';color:beige\n"
"font-size:70px;\n"
"")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.M_Name = QtWidgets.QLineEdit(self.frame)
        self.M_Name.setGeometry(QtCore.QRect(170, 170, 311, 31))
        self.M_Name.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.M_Name.setObjectName("M_Name")

        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(540, 140, 121, 16))
        self.label_9.setStyleSheet("font: 10pt  \"MS Shell Dlg 2\";color:beige\n"
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
        self.RefNo = QtWidgets.QLineEdit(self.frame)
        self.RefNo.setGeometry(QtCore.QRect(170, 290, 311, 31))
        self.RefNo.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.RefNo.setText("")
        self.RefNo.setPlaceholderText("")
        self.RefNo.setObjectName("RefNo")
        self.H_No = QtWidgets.QLineEdit(self.frame)
        self.H_No.setGeometry(QtCore.QRect(670, 130, 311, 31))
        self.H_No.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.H_No.setObjectName("H_No")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(40, 340, 121, 16))
        self.label_15.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_15.setObjectName("label_15")

        self.passwrd = QtWidgets.QLineEdit(self.frame)
        self.passwrd.setGeometry(QtCore.QRect(170, 330, 311, 31))
        self.passwrd.setStyleSheet("border:none;\ncolor:beige"
                                  "border-bottom:1px solid black;")
        self.passwrd.setObjectName("nation")


        self.trying = QtWidgets.QLabel(self.frame)
        self.trying.setGeometry(QtCore.QRect(40, 370, 121, 16))
        self.trying.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
                                    "")
        self.trying.setObjectName("trying")

        self.nation = QtWidgets.QLineEdit(self.frame)
        self.nation.setGeometry(QtCore.QRect(170, 370, 311, 31))
        self.nation.setStyleSheet("border:none;\ncolor:beige"
                                   "border-bottom:1px solid black;")
        self.nation.setObjectName("nation")



        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 260, 121, 16))
        self.label_13.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_13.setObjectName("label_13")
        self.F_Name = QtWidgets.QLineEdit(self.frame)
        self.F_Name.setGeometry(QtCore.QRect(170, 130, 311, 31))
        self.F_Name.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.F_Name.setObjectName("F_Name")
        self.U_City = QtWidgets.QLineEdit(self.frame)
        self.U_City.setGeometry(QtCore.QRect(670, 250, 311, 31))
        self.U_City.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.U_City.setObjectName("U_City")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(40, 300, 121, 16))
        self.label_14.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")

        self.label_14.setObjectName("label_14")

        self.Street_No = QtWidgets.QLineEdit(self.frame)
        self.Street_No.setGeometry(QtCore.QRect(670, 170, 311, 31))
        self.Street_No.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")

        self.Street_No.setText("")

        self.Street_No.setObjectName("Street_No")
        self.L_Name = QtWidgets.QLineEdit(self.frame)
        self.L_Name.setGeometry(QtCore.QRect(170, 210, 311, 31))
        self.L_Name.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.L_Name.setText("")
        self.L_Name.setObjectName("L_Name")

        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(540, 220, 121, 16))
        self.label_11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(540, 300, 121, 16))
        self.label_16.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")

        self.T_add = QtWidgets.QLineEdit(self.frame)
        self.T_add.setGeometry(QtCore.QRect(170, 250, 311, 31))
        self.T_add.setStyleSheet("border:none;\n"
                                   "border-bottom:1px solid black;")
        self.T_add.setObjectName("T_add")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setObjectName("label_16")

        self.Gender = QtWidgets.QLineEdit(self.frame)
        self.Gender.setGeometry(QtCore.QRect(670, 290, 311, 31))
        self.Gender.setStyleSheet("border:none;\ncolor:beige"
                                   "border-bottom:1px solid black;")

        self.Gender.setObjectName("Passwrd")

        self.issue = QtWidgets.QLabel(self.frame)
        self.issue.setGeometry(QtCore.QRect(540, 340, 121, 16))
        self.issue.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
                                    "")
        self.issue.setObjectName("issue ")
        self.issue_date = QtWidgets.QLineEdit(self.frame)
        self.issue_date.setGeometry(QtCore.QRect(670, 330, 311, 31))
        self.issue_date.setStyleSheet("border:none;\ncolor:beige"
                                  "border-bottom:1px solid black;")

        self.issue_date.setObjectName("issue date")




        self.expiry = QtWidgets.QLabel(self.frame)
        self.expiry.setGeometry(QtCore.QRect(535, 370, 121, 16))
        self.expiry.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
                                    "")
        self.expiry.setObjectName("issue ")
        self.expiry_date = QtWidgets.QLineEdit(self.frame)
        self.expiry_date.setGeometry(QtCore.QRect(670, 370, 311, 31))
        self.expiry_date.setStyleSheet("border:none;\ncolor:beige"
                                  "border-bottom:1px solid black;")

        self.expiry_date.setObjectName("issue date")








        self.U_Division = QtWidgets.QLineEdit(self.frame)
        self.U_Division.setGeometry(QtCore.QRect(670, 210, 311, 31))
        self.U_Division.setStyleSheet("border:none;\ncolor:beige"
"border-bottom:1px solid black;")
        self.U_Division.setObjectName("U_Division")
        self.MeterNo = QtWidgets.QLineEdit(self.frame)
        self.MeterNo.setGeometry(QtCore.QRect(170, 250, 311, 31))
        self.MeterNo.setStyleSheet("border:none;\ncolor:beige"
"border-bottom:1px solid black;")
        self.MeterNo.setObjectName("MeterNo")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\"; color:beige\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 180, 121, 16))
        self.label_12.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(540, 260, 121, 16))
        self.label_17.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";color:beige\n"
"")
        self.label_17.setObjectName("label_17")

        self.ExitButton = QtWidgets.QPushButton(self.frame)
        self.ExitButton.setGeometry(QtCore.QRect(600, 450, 251, 51))
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitButton.setStyleSheet("QPushButton{\n"
                                      "background-color:rgb(52, 45, 113);\n"
                                      "color:white;\n"
                                      "border-radius:20px;\n"
                                      "font-size:20px;\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "\n"
                                      "background-color: white;\n"
                                      "color:rgb(52, 45, 113);\n"
                                      "border:1px solid rgb(52, 45, 113);\n"
                                      "transform:scale(1.2);\n"
                                      "\n"
                                      "}")
        self.ExitButton.clicked.connect(lambda: self.openWindow())
        self.ExitButton.setObjectName("ExitButton")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.clicked.connect(lambda: self.activate())
        self.pushButton_7.setGeometry(QtCore.QRect(200, 450, 251, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"background-color:rgb(52, 45, 113);\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(52, 45, 113);\n"
"border:1px solid rgb(52, 45, 113);\n"
"transform:scale(1.2);\n"
"\n"
"}")
        self.pushButton_7.clicked.connect(lambda: self.activate())
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(400, 60, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 30px ;color:beige\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", " "))
        self.label_16.setText(_translate("Dialog", "Gender"))
        self.Gender.setPlaceholderText(_translate("Dialog", "Enter your Gender "))
        self.issue.setText(_translate("Dialog", "Issue Date "))
        self.issue_date.setPlaceholderText(_translate("Dialog", "Enter Issue date "))
        self.expiry.setText(_translate("Dialog", " Expiry Date "))
        self.expiry_date.setPlaceholderText(_translate("Dialog", "Enter Expiry date "))

        self.label_9.setText(_translate("Dialog", "Contact info  "))
        self.H_No.setPlaceholderText(_translate("Dialog", "03-xxxxxxx-xx"))
        self.label_10.setText(_translate("Dialog", " Disability "))
        self.Street_No.setPlaceholderText(_translate("Dialog", "Disability(if any)"))
        self.label_12.setText(_translate("Dialog", "CNIC no."))
        self.M_Name.setPlaceholderText(_translate("Dialog", "e.g. xxxxx-xxxxxxx-x"))
        self.label_8.setText(_translate("Dialog", "First Name"))
        self.L_Name.setPlaceholderText(_translate("Dialog", "e.g. izza"))

        self.label_15.setText(_translate("Dialog", "Address"))
        self.label_13.setText(_translate("Dialog", "Last Name"))
        self.MeterNo.setPlaceholderText(_translate("Dialog", "e.g shahzad  "))

        self.U_City.setPlaceholderText(_translate("Dialog", "e.g. Islamabad"))
        self.label_14.setText(_translate("Dialog", "DOB  "))
        self.RefNo.setPlaceholderText(_translate("Dialog", "DD/MM/YYY"))
        self.T_add.setPlaceholderText(_translate("Dialog", "e.g. hsue"))


        self.label_11.setText(_translate("Dialog", "Province"))
        self.U_Division.setPlaceholderText(_translate("Dialog", " e.g. Punjab"))

        self.passwrd.setPlaceholderText(_translate("Dialog", ""))

        self.trying.setText(_translate("Dialog", "Nationality"))
        self.nation.setPlaceholderText(_translate("Dialog", "e.g. Pakistani"))


        self.label_7.setText(_translate("Dialog", "Passport No."))
        self.F_Name.setPlaceholderText(_translate("Dialog", "Enter Passport no."))


        self.label_17.setText(_translate("Dialog", "City"))
        self.pushButton_7.setText(_translate("Dialog", "Activate/renew "))

        self.ExitButton.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Passport Activation "))

    def activate(self):
        msg = QMessageBox()
        if (
                self.F_Name.text() == ""
                or self.MeterNo.text() == ""
                or self.passwrd.text() == ""
        ):
            msg.setText("Fill All Required Fields")
            msg.setWindowTitle("Error")
            w = msg.exec_()
        else:
            try:
                Passport_no = self.F_Name.text()
                CNIC_no = int(self.M_Name.text())
                First_name = self.L_Name.text()
                Last_name = self.MeterNo.text()
                DOB = self.RefNo.text()
                address = self.nation.text()
                Nationality = self.passwrd.text()
                Contact_info = self.H_No.text()
                Disability = self.Street_No.text()
                Province = self.U_Division.text()
                City = self.U_City.text()
                Gender = self.Gender.text()
                Issue_date = self.issue_date.text()
                Expiry_date = self.expiry_date.text()

                with cx_Oracle.connect('system/Oracle_1') as co:
                    cur = co.cursor()

                    sql9 = """
                        INSERT INTO PASS_ACTIVATION 
                        VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)
                    """
                    cur.execute(
                        sql9,
                        [

                            Passport_no,
                            CNIC_no,
                            First_name,
                            Last_name,
                            DOB,
                            address,
                            Nationality,
                            Contact_info,
                            Disability,
                            Province,
                            City,
                            Gender,
                            Issue_date,
                            Expiry_date,
                        ],
                    )

                    co.commit()

                    msg = QMessageBox()
                    msg.setText("Congratulations! Your passport is activated  successfully")
                    msg.setWindowTitle("Success")
                    w = msg.exec_()

            except cx_Oracle.Error as error:
                print("Oracle Error:", error)
                msg = QMessageBox()

                w = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = pass_acti()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
