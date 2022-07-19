from J import Ui_MainWindow
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
        print("_________M_________")
        Jarvis.Main()


startExe = MainThread()

class GUI_MOVIE(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        # self.gui.btn_start.clicked(self.startTask)
        self.gui.btn_start.clicked.connect(self.startTask)
        self.gui.btn_stop.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1 = QtGui.QMovie(
            "public//initial.gif"
        )
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie(
            "public//live.gif"
        )
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label4 = QtGui.QMovie(
            "public//ring.gif"
        )
        self.gui.gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(10)
        startExe.start()


    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.gui.ojb_t1.setText(label_date)
        self.gui.obj_t2.setText(label_time)
        


GUIApp = QApplication(sys.argv)
jarvis_GUI = GUI_MOVIE()
jarvis_GUI.show()
exit(GUIApp.exec_())
