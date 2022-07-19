# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jarvis_1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1635, 886)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.BG_black = QLabel(self.centralwidget)
        self.BG_black.setObjectName(u"BG_black")
        self.BG_black.setGeometry(QRect(0, 0, 1920, 1080))
        self.BG_black.setAutoFillBackground(True)
        self.BG_black.setPixmap(QPixmap(u"../Desktop/G.U.I Material/B.G/Black_Template.jpg"))
        self.BG_black.setScaledContents(True)
        self.BG_black.setWordWrap(False)
        self.bg_2 = QLabel(self.centralwidget)
        self.bg_2.setObjectName(u"bg_2")
        self.bg_2.setGeometry(QRect(10, 70, 361, 141))
        self.bg_2.setAutoFillBackground(False)
        self.bg_2.setStyleSheet(u"background-color:rgb(170, 85, 255)")
        self.bg_3 = QLabel(self.centralwidget)
        self.bg_3.setObjectName(u"bg_3")
        self.bg_3.setGeometry(QRect(380, 10, 1241, 611))
        self.bg_3.setAutoFillBackground(False)
        self.bg_3.setStyleSheet(u"background-color:rgb(170, 85, 255)")
        self.bg_3.setScaledContents(True)
        self.gif_1 = QLabel(self.centralwidget)
        self.gif_1.setObjectName(u"gif_1")
        self.gif_1.setGeometry(QRect(20, 80, 341, 121))
        self.gif_1.setPixmap(QPixmap(u"../Desktop/G.U.I Material/ExtraGui/initial.gif"))
        self.gif_1.setScaledContents(True)
        self.gif_2 = QLabel(self.centralwidget)
        self.gif_2.setObjectName(u"gif_2")
        self.gif_2.setGeometry(QRect(390, 20, 1221, 591))
        self.gif_2.setPixmap(QPixmap(u"../Desktop/G.U.I Material/ExtraGui/live.gif"))
        self.gif_2.setScaledContents(True)
        self.gif_4 = QLabel(self.centralwidget)
        self.gif_4.setObjectName(u"gif_4")
        self.gif_4.setGeometry(QRect(20, 290, 341, 271))
        self.gif_4.setPixmap(QPixmap(u"../Desktop/G.U.I Material/VoiceReg/Ntuks.gif"))
        self.gif_4.setScaledContents(True)
        self.txt_time = QLabel(self.centralwidget)
        self.txt_time.setObjectName(u"txt_time")
        self.txt_time.setGeometry(QRect(30, 570, 341, 271))
        self.txt_time.setStyleSheet(u"background-color:Transparent;\n"
"")
        self.txt_time.setPixmap(QPixmap(u"../Desktop/G.U.I Material/B.G/gyhf.jpg"))
        self.txt_time.setScaledContents(True)
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(1280, 630, 321, 91))
        self.btn_start.setStyleSheet(u"background-color:transparent;\n"
"")
        self.bg_4 = QLabel(self.centralwidget)
        self.bg_4.setObjectName(u"bg_4")
        self.bg_4.setGeometry(QRect(1250, 620, 361, 111))
        self.bg_4.setAutoFillBackground(False)
        self.bg_4.setStyleSheet(u"background-color:rgb(170, 85, 255)")
        self.bg_4.setPixmap(QPixmap(u"../Desktop/G.U.I Material/Buttons/Start.png"))
        self.bg_4.setScaledContents(True)
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(1280, 730, 321, 91))
        self.btn_stop.setStyleSheet(u"background-color:transparent;\n"
"")
        self.bg_5 = QLabel(self.centralwidget)
        self.bg_5.setObjectName(u"bg_5")
        self.bg_5.setGeometry(QRect(1260, 720, 361, 111))
        self.bg_5.setAutoFillBackground(False)
        self.bg_5.setStyleSheet(u"background-color:rgb(170, 85, 255)")
        self.bg_5.setPixmap(QPixmap(u"../Desktop/G.U.I Material/Buttons/Quit.png"))
        self.bg_5.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.BG_black.raise_()
        self.bg_2.raise_()
        self.bg_3.raise_()
        self.gif_1.raise_()
        self.gif_2.raise_()
        self.gif_4.raise_()
        self.txt_time.raise_()
        self.bg_4.raise_()
        self.btn_start.raise_()
        self.bg_5.raise_()
        self.btn_stop.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1635, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BG_black.setText("")
        self.bg_2.setText("")
        self.bg_3.setText("")
        self.gif_1.setText("")
        self.gif_2.setText("")
        self.gif_4.setText("")
        self.txt_time.setText("")
        self.btn_start.setText("")
        self.bg_4.setText("")
        self.btn_stop.setText("")
        self.bg_5.setText("")
    # retranslateUi

