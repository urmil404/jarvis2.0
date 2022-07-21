from J import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUi
import sys
import Jarvis_old
from Task import wishMe
import random
import json
import re
import torch
from Brain import NeuralNet
from NeauralNetwork import bag_of_words, tokenize
from datetime import datetime
from Listen import Suno
from Speak import Bol
from Task import NonInputExecution
from Task import InputExecution


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
with open("intents.json", "r") as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()



Name = "JARVIS"


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

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
        self.gui.label1 = QtGui.QMovie("public//initial.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("public//live.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label4 = QtGui.QMovie("public//ring.gif")
        self.gui.gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        wishMe()

        self.gui.txt_final.setText("Listening...")

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(10)
        startExe.start()

        while True:
            sentence = Suno()
            result = str(sentence)
            if sentence == "bye bye":
                exit()
            else:
                self.gui.txt_final.setText(sentence)

            sentence = tokenize(sentence)
            X = bag_of_words(sentence, all_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X).to(device)

            output = model(X)
            _, predicted = torch.max(output, dim=1)

            tag = tags[predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]

            if prob.item() > 0.75:
                for intent in intents["intents"]:
                    if tag == intent["tag"]:
                        reply = random.choice(intent["responses"])
                        if "time" in reply:
                            NonInputExecution(reply)
                        elif "date" in reply:
                            NonInputExecution(reply)
                        elif "day" in reply:
                            NonInputExecution(reply)
                        elif "wikipedia" in reply:
                            InputExecution(reply, sentence)
                        elif "google" in reply:
                            InputExecution(reply, result)
                        elif "joke" in reply:
                            NonInputExecution(reply)
                        else:
                            Bol(reply)

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.gui.ojb_t1.setText(label_date)
        self.gui.obj_t2.setText(label_time)


GUIApp = QApplication(sys.argv)
jarvis_GUI = GUI_MOVIE()
jarvis_GUI.show()
exit(GUIApp.exec_())
