from jarvisUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUi
import sys
import Jarvis


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        Jarvis.Main()


startExe = MainThread()


class Gui_Start(QMainWindow):
    def __init__(self):

        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.btn_start.clicked.connect(self.startTask)
        self.gui.btn_stop.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1 = QtGui.QMovie(
            "..//Desktop//G.U.I Material//ExtraGui//initial.gif"
        )
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie(
            "..//Desktop//G.U.I Material//ExtraGui//live.gif"
        )
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label4 = QtGui.QMovie(
            "..//Desktop//G.U.I Material//VoiceReg//Ntuks.gif"
        )
        self.gui.gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("..//Desktop//G.U.I Material//B.G//gyhf.jpg")
        self.gui.txt_time.setMovie(self.gui.label5)
        self.gui.label5.start()

        startExe.start()


GuiApp = QApplication(sys.argv)
jarvis_GUI = Gui_Start()
jarvis_GUI.show()
exit(GuiApp.exec_())
