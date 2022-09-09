from Speak import Bol
import pyjokes
import weather
import datetime
from datetime import datetime as dt
from PyQt5.QtCore import Qt, QTime, QDate
import wikipedia
import pywhatkit
from News import news


def Time():
    time = dt.now().strftime("%H:%M")
    Bol(time)


def Date():
    date = datetime.date.today()
    Bol(date)


def Day():
    day = dt.now().strftime("%A")
    Bol(day)


def Joke(ref):
    funny = pyjokes.get_joke()
    ref.gui.speaker.setText(funny)
    Bol(funny)

def music():
    funny = pyjokes.get_joke()
    Bol(funny)

def NonInputExecution(query, ref = None):
    query = str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    elif "joke" in query:
        Joke(ref)
    elif "weather" in query:
        weather.weathernews(ref)
    elif "news" in query:
        news(ref)
    elif "music" in query:
        music()


def wishMe(ref=None):
    hour = int(dt.now().hour)
    if hour >= 0 and hour <= 12:
        Bol("Good Morning")
    elif hour >= 12 and hour <= 18:
        Bol("Good Afternoon")
    else:
        Bol("Good Evening")

    ref.gui.listener.setText("Thinking...")
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


def InputExecution(tag, query,ref=None):
    if "wikipedia" in tag:
        try:
            name = str(query).replace("about", "").replace("wikipedia", "")
            result = wikipedia.summary(name, sentences=2)
            ref.gui.speaker.setText(result)
            Bol(result)
        except:
            Bol("Sorry, I could not find any result")
    
    elif "music" in tag:
        print("playing music...")
        query = str(query).replace("youtube", "")
        query = query.replace("on youtube", "")
        pywhatkit.playonyt(query + "music")
        
        
    elif "youtube" in tag:
        print("youtubing...")
        query = str(query).replace("youtube", "")
        query = query.replace("on youtube", "")
        pywhatkit.playonyt(query)
        

    elif "google" in tag:
        print("Googling...")
        query = str(query).replace("google", "")
        query = query.replace("google search", "")
        query = query.replace("search", "")
        query = query.replace("who is", "")
        query = query.replace("about", "")
        pywhatkit.search(query)
