from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsPage(object):
    def setupUi(self, settingsPage):
        settingsPage.setObjectName("settingsPage")
        settingsPage.resize(1131, 705)
        settingsPage.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        settingsPage.setAttribute(QtCore.Qt.WA_TranslucentBackground)   
        self.mainFrame = QtWidgets.QFrame(settingsPage)
        self.mainFrame.setGeometry(QtCore.QRect(80, 70, 981, 551))
        self.mainFrame.setStyleSheet("QFrame {\n"
"\n"
"background-color: #181818;\n"
"border: none;\n"
"border-radius: 15px;\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.frameLeft = QtWidgets.QFrame(self.mainFrame)
        self.frameLeft.setGeometry(QtCore.QRect(0, 0, 61, 551))
        self.frameLeft.setStyleSheet("QFrame {\n"
"border: none;\n"
"background-color: #841414\n"
"\n"
"}")
        self.frameLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLeft.setObjectName("frameLeft")
        self.frameDiv_2 = QtWidgets.QFrame(self.frameLeft)
        self.frameDiv_2.setGeometry(QtCore.QRect(16, 50, 29, 3))
        self.frameDiv_2.setStyleSheet("QFrame {\n"
"\n"
"background: #181818;\n"
"border-radius: 5px\n"
"\n"
"}")
        self.frameDiv_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDiv_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDiv_2.setObjectName("frameDiv_2")
        self.buttonHome = QtWidgets.QPushButton(self.frameLeft)
        self.buttonHome.setGeometry(QtCore.QRect(10, 90, 41, 41))
        self.buttonHome.setStyleSheet("QPushButton {\n"
"border: none\n"
"}\n"
"QPushButton:pressed {\n"
"border: none;\n"
"background: #181818;\n"
"border-radius: 15px;\n"
"}")
        self.buttonHome.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Settings_Button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonHome.setIcon(icon)
        self.buttonHome.setIconSize(QtCore.QSize(26, 26))
        self.buttonHome.setObjectName("buttonHome")
        self.buttonSettings = QtWidgets.QPushButton(self.frameLeft)
        self.buttonSettings.setGeometry(QtCore.QRect(10, 140, 41, 41))
        self.buttonSettings.setStyleSheet("QPushButton {\n"
"border: none\n"
"}\n"
"QPushButton:pressed {\n"
"border: none;\n"
"background: #281818;\n"
"border-radius: 15px;\n"
"}")
        self.buttonSettings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Study timer project/Settings_Button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSettings.setIcon(icon1)
        self.buttonSettings.setIconSize(QtCore.QSize(26, 26))
        self.buttonSettings.setObjectName("buttonSettings")
        self.frameTop = QtWidgets.QFrame(self.mainFrame)
        self.frameTop.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.frameTop.setStyleSheet("QFrame {\n"
"border: none;\n"
"background: #141414;\n"
"background-color: #841414; \n"
"}")
        self.frameTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTop.setObjectName("frameTop")
        self.buttonClose = QtWidgets.QPushButton(self.frameTop)
        self.buttonClose.setGeometry(QtCore.QRect(947, 10, 31, 31))
        self.buttonClose.setStyleSheet("QPushButton {\n"
"\n"
"border: none\n"
"\n"
"\n"
"}")
        self.buttonClose.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Study timer project/Settings_Button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonClose.setIcon(icon2)
        self.buttonClose.setIconSize(QtCore.QSize(25, 20))
        self.buttonClose.setObjectName("buttonClose")
        self.buttonMinim = QtWidgets.QPushButton(self.frameTop)
        self.buttonMinim.setGeometry(QtCore.QRect(920, 10, 31, 31))
        self.buttonMinim.setStyleSheet("QPushButton {\n"
"\n"
"border: none\n"
"\n"
"\n"
"}")
        self.buttonMinim.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Study timer project/Settings_Button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonMinim.setIcon(icon3)
        self.buttonMinim.setIconSize(QtCore.QSize(25, 20))
        self.buttonMinim.setObjectName("buttonMinim")
        self.lblHomepage = QtWidgets.QLabel(self.frameTop)
        self.lblHomepage.setGeometry(QtCore.QRect(90, 8, 121, 31))
        self.lblHomepage.setStyleSheet("QLabel {\n"
"color: #efefef;\n"
"font: 63 16pt \"Raleway SemiBold\";\n"
"\n"
"}")
        self.lblHomepage.setObjectName("lblHomepage")
        self.frameDiv_1 = QtWidgets.QFrame(self.frameTop)
        self.frameDiv_1.setGeometry(QtCore.QRect(60, 10, 2, 29))
        self.frameDiv_1.setStyleSheet("QFrame {\n"
"\n"
"background: #181818;\n"
"border-radius: 5px\n"
"\n"
"}")
        self.frameDiv_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDiv_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDiv_1.setObjectName("frameDiv_1")
        self.buttonIcon = QtWidgets.QPushButton(self.frameTop)
        self.buttonIcon.setGeometry(QtCore.QRect(11, 7, 41, 41))
        self.buttonIcon.setStyleSheet("QPushButton {\n"
"\n"
"border: none\n"
"\n"
"\n"
"}")
        self.buttonIcon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Study timer project/Settings_Button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIcon.setIcon(icon4)
        self.buttonIcon.setIconSize(QtCore.QSize(55, 55))
        self.buttonIcon.setObjectName("buttonIcon")
        self.frameUnder = QtWidgets.QFrame(self.mainFrame)
        self.frameUnder.setGeometry(QtCore.QRect(0, 520, 981, 31))
        self.frameUnder.setStyleSheet("QFrame {\n"
"border: none;\n"
"background: #141414;\n"
"border-top-right-radius: none;\n"
"border-bottom-left-radius: none;\n"
"\n"
"}")
        self.frameUnder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameUnder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameUnder.setObjectName("frameUnder")
        self.labelCredits = QtWidgets.QLabel(self.frameUnder)
        self.labelCredits.setGeometry(QtCore.QRect(915, 5, 61, 21))
        self.labelCredits.setStyleSheet("QLabel {\n"
"\n"
"color: #505050;\n"
"font: 63 10pt \"Raleway SemiBold\";\n"
"\n"
"}")
        self.labelCredits.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelCredits.setObjectName("labelCredits")
        self.textUsername_5 = QtWidgets.QLabel(self.mainFrame)
        self.textUsername_5.setGeometry(QtCore.QRect(105, 80, 81, 21))
        self.textUsername_5.setStyleSheet("QLabel {\n"
"\n"
"border: none;\n"
"color: #3fefef;\n"
"font: 57 9pt \"Raleway SemiBold\";\n"
"background: #181818;\n"
"\n"
"}")
        self.textUsername_5.setAlignment(QtCore.Qt.AlignCenter)
        self.textUsername_5.setObjectName("textUsername_5")
        self.frame = QtWidgets.QFrame(self.mainFrame)
        self.frame.setGeometry(QtCore.QRect(90, 90, 171, 41))
        self.frame.setStyleSheet("QFrame {\n"
"\n"
"border: 2px Solid #efefef;\n"
"border-radius: 13px;\n"
"background: #171717;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 9, 151, 21))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"border: none;\n"
"color: #efefef;\n"
"font: 63 10pt \"Raleway SemiBold\";\n"
"background: #181818\n"
"\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.frame.raise_()
        self.frameLeft.raise_()
        self.frameTop.raise_()
        self.frameUnder.raise_()
        self.textUsername_5.raise_()

        self.retranslateUi(settingsPage)
        QtCore.QMetaObject.connectSlotsByName(settingsPage)

    def retranslateUi(self, settingsPage):
        _translate = QtCore.QCoreApplication.translate
        settingsPage.setWindowTitle(_translate("settingsPage", "Form"))
        self.lblHomepage.setText(_translate("settingsPage", "Settings"))
        self.labelCredits.setText(_translate("settingsPage", "by gxzs"))
        self.textUsername_5.setText(_translate("settingsPage", "Interval (ms)"))
        self.lineEdit.setPlaceholderText(_translate("settingsPage", "0.001"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsPage = QtWidgets.QWidget()
    ui = Ui_settingsPage()
    ui.setupUi(settingsPage)
    settingsPage.show()
    sys.exit(app.exec_())