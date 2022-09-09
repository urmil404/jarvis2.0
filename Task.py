from Speak import Bol
import pyjokes
# import datetime
from datetime import datetime
from PyQt5.QtCore import Qt, QTime, QDate

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Bol(time)


def Date():
    date = datetime.date.today()
    Bol(date)


def Day():
    day = datetime.now().strftime("%A")
    Bol(day)


def Joke():
    funny = pyjokes.get_joke()
    Bol(funny)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    elif "joke" in query:
        Joke()


def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        Bol("Good Morning")
    elif hour >= 12 and hour <= 18:
        Bol("Good Afternoon")
    else:
        Bol("Good Evening")

    Bol("Jarvis here, Hello Sir")
    Bol("Today is")
    Day()

class Tasking:
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.gui.ojb_t1.setText(label_date)
        self.gui.obj_t2.setText(label_time)


def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("about", "").replace("wikipedia", "")
        import wikipedia

        result = wikipedia.summary(name, sentences=2)
        Bol(result)

    elif "google" in tag:
        print("Googling...")
        query = str(query).replace("google", "")
        query = query.replace("google search", "")
        query = query.replace("search", "")
        query = query.replace("who is", "")
        query = query.replace("about", "")
        import pywhatkit

        pywhatkit.search(query)
