# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'J.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1635, 886)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BG_black = QtWidgets.QLabel(self.centralwidget)
        self.BG_black.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.BG_black.setAutoFillBackground(True)
        self.BG_black.setText("")
        self.BG_black.setPixmap(QtGui.QPixmap("../G.U.I Material/B.G/Black_Template.jpg"))
        self.BG_black.setScaledContents(True)
        self.BG_black.setWordWrap(False)
        self.BG_black.setObjectName("BG_black")
        self.bg_2 = QtWidgets.QLabel(self.centralwidget)
        self.bg_2.setGeometry(QtCore.QRect(10, 70, 361, 141))
        self.bg_2.setAutoFillBackground(False)
        self.bg_2.setStyleSheet("background-color:transparent")
        self.bg_2.setText("")
        self.bg_2.setObjectName("bg_2")
        self.bg_3 = QtWidgets.QLabel(self.centralwidget)
        self.bg_3.setGeometry(QtCore.QRect(380, 10, 1211, 451))
        self.bg_3.setAutoFillBackground(False)
        self.bg_3.setStyleSheet("background-color:transparent")
        self.bg_3.setText("")
        self.bg_3.setScaledContents(True)
        self.bg_3.setObjectName("bg_3")
        self.gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(20, 30, 341, 121))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap("../G.U.I Material/ExtraGui/initial.gif"))
        self.gif_1.setScaledContents(True)
        self.gif_1.setObjectName("gif_1")
        self.gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.gif_2.setGeometry(QtCore.QRect(400, 70, 1171, 371))
        self.gif_2.setText("")
        self.gif_2.setPixmap(QtGui.QPixmap("../G.U.I Material/ExtraGui/live.gif"))
        self.gif_2.setScaledContents(True)
        self.gif_2.setObjectName("gif_2")
        self.gif_4 = QtWidgets.QLabel(self.centralwidget)
        self.gif_4.setGeometry(QtCore.QRect(30, 220, 341, 271))
        self.gif_4.setText("")
        self.gif_4.setPixmap(QtGui.QPixmap("../G.U.I Material/VoiceReg/Ntuks.gif"))
        self.gif_4.setScaledContents(True)
        self.gif_4.setObjectName("gif_4")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(1280, 630, 321, 91))
        self.btn_start.setStyleSheet("background-color:transparent;\n"
"")
        self.btn_start.setText("")
        self.btn_start.setObjectName("btn_start")
        self.bg_4 = QtWidgets.QLabel(self.centralwidget)
        self.bg_4.setGeometry(QtCore.QRect(1250, 620, 361, 111))
        self.bg_4.setAutoFillBackground(False)
        self.bg_4.setStyleSheet("background-color:rgb(170, 85, 255)")
        self.bg_4.setText("")
        self.bg_4.setPixmap(QtGui.QPixmap("../G.U.I Material/Buttons/Start.png"))
        self.bg_4.setScaledContents(True)
        self.bg_4.setObjectName("bg_4")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(1280, 730, 321, 91))
        self.btn_stop.setStyleSheet("background-color:transparent;\n"
"")
        self.btn_stop.setText("")
        self.btn_stop.setObjectName("btn_stop")
        self.bg_5 = QtWidgets.QLabel(self.centralwidget)
        self.bg_5.setGeometry(QtCore.QRect(1260, 720, 361, 111))
        self.bg_5.setAutoFillBackground(False)
        self.bg_5.setStyleSheet("background-color:rgb(170, 85, 255)")
        self.bg_5.setText("")
        self.bg_5.setPixmap(QtGui.QPixmap("../G.U.I Material/Buttons/Quit.png"))
        self.bg_5.setScaledContents(True)
        self.bg_5.setObjectName("bg_5")
        self.ojb_t1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.ojb_t1.setGeometry(QtCore.QRect(110, 560, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(26)
        font.setItalic(False)
        self.ojb_t1.setFont(font)
        self.ojb_t1.setAutoFillBackground(False)
        self.ojb_t1.setStyleSheet("background-color:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"text-align:center;")
        self.ojb_t1.setObjectName("ojb_t1")
        self.obj_t2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.obj_t2.setGeometry(QtCore.QRect(100, 690, 381, 111))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(26)
        font.setItalic(False)
        self.obj_t2.setFont(font)
        self.obj_t2.setStyleSheet("background-color:transparent;\n"
"border-radius:none;\n"
"color:white;")
        self.obj_t2.setObjectName("obj_t2")
        self.speaker = QtWidgets.QTextBrowser(self.centralwidget)
        self.speaker.setGeometry(QtCore.QRect(430, 650, 801, 161))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        self.speaker.setFont(font)
        self.speaker.setStyleSheet("background-color:transparant;\n"
"color:rgb(255, 255, 0);")
        self.speaker.setObjectName("speaker")
        self.listener = QtWidgets.QTextBrowser(self.centralwidget)
        self.listener.setGeometry(QtCore.QRect(430, 480, 801, 161))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(28)
        self.listener.setFont(font)
        self.listener.setStyleSheet("background-color:transparant;\n"
"color:green;")
        self.listener.setObjectName("listener")
        self.BG_black.raise_()
        self.bg_2.raise_()
        self.bg_3.raise_()
        self.gif_1.raise_()
        self.gif_2.raise_()
        self.gif_4.raise_()
        self.bg_4.raise_()
        self.btn_start.raise_()
        self.bg_5.raise_()
        self.btn_stop.raise_()
        self.ojb_t1.raise_()
        self.obj_t2.raise_()
        self.speaker.raise_()
        self.listener.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1635, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ojb_t1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Maiandra GD\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Dubai Medium\'; font-size:36pt; color:#ffff00;\">Date</span></p></body></html>"))
        self.obj_t2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Maiandra GD\'; font-size:26pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Dubai Medium\'; font-size:36pt; color:#ffff00;\">Time</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
