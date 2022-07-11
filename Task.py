import datetime
from Speak import Bol


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Bol(time)


def Date():
    date = datetime.date.today()
    Bol(date)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Bol(day)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()


def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("about", "").replace("wikipedia", "")
        import wikipedia

        result = wikipedia.summary(name, sentences=2)
        Bol(result)

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("google search", "")
        query = query.replace("search", "")
        query = query.replace("who is", "")
        query = query.replace("about", "")
        import pywhatkit
        pywhatkit.search(query)
