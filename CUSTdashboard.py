# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FAfterLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from passapplication import pass_form
from applicationfee import Trans
from customerfeedback import FB


class AfterLogin(object):
    def window1(self):
        self.window = QtWidgets.QDialog()
        self.ui = pass_form()
        self.ui.setupUi(self.window)
        self.window.show()
    def window2(self):
        self.window = QtWidgets.QDialog()
        self.ui = Trans()
        self.ui.setupUi(self.window)
        self.window.show()

    def window3(self):
        self.window = QtWidgets.QDialog()
        self.ui = FB()
        self.ui.setupUi(self.window)
        self.window.show()




    def window4(self):
        exit()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setAutoFillBackground(True)

        self.widget.setStyleSheet("background-image: url(E:/downloads/side-view-valet-doing-his-job.jpg)\n"
"background-repeat:no-repeat;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(40, 40, 50, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("QFrame#frame\n"
"{\n"
"background-color:#013220;\n"
"border-radius:10px;\n"
"};")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.picture= QtWidgets.QLabel(self.frame)
        self.picture.setGeometry(QtCore.QRect(600, 0, 700, 550))
        self.picture.setStyleSheet("background-image: url(E:/downloads/passport.webp);")
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("E:/downloads/passport.webp"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("label_2")


        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 50, 271, 41))
        self.label.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:30px;color:beige\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 491, 91))
        self.label_2.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:15px;\n"
"line-height:2px;color:beige\n"
"")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 420, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2,color:beige")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.clicked.connect(lambda: self.window4())
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 300, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton:hover{\n"
"background-color:rgb(30,144,255);\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton\n"
"{\n"
"border-radius:20px;\n"
"background-color: white;\n"
"color:black;\n"
"border:1px solid rgb(30,144,255);\n"
"transform:scale(1.2);\n"
"\n"
"}")
        self.pushButton_3.clicked.connect(lambda: self.window2())
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 360, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton:hover{\n"
                                        "background-color:rgb(30,144,255);\n"
                                        "color:white;\n"
                                        "border-radius:20px;\n"
                                        "}\n"
                                        "QPushButton\n"
                                        "{\n"
                                        "border-radius:20px;\n"
                                        "background-color: white;\n"
                                        "color:black;\n"
                                        "border:1px solid rgb(30,144,255);\n"
                                        "transform:scale(1.2);\n"
                                        "\n"
                                        "}")
        self.pushButton_5.clicked.connect(lambda: self.window3())
        self.pushButton_5.setObjectName("pushButton_3")



        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 240, 201, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
"padding:10px;\n"
"}")
        self.pushButton_4.clicked.connect(lambda: self.window1())
        self.pushButton_4.setObjectName("pushButton_4")



        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(640, 50, 421, 411))
        self.label_3.setStyleSheet("\n"
"background-image: url(:/downloads/passport.webp);\n"
"background-repeat:no-repeat;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome Back:)"))
        self.label_2.setText(_translate("Dialog", "PMS is a digital platform  for issuance renewal of passports. \n"
"It provides a user-friendly experience to the customers. \n")
                             )
        self.pushButton_2.setText(_translate("Dialog", "Exit"))
        self.pushButton_5.setText(_translate("Dialog", "Customer Support   "))
        self.pushButton_3.setText(_translate("Dialog", "Application  Fee "))
        self.pushButton_4.setText(_translate("Dialog", " Application Submission "))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AfterLogin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
