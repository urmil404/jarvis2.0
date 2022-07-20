from datetime import datetime
from Speak import Bol

def wishMe(self):
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        Bol("Good Morning")
    elif hour >= 12 and hour <= 18:
        Bol("Good Afternoon")
    else:
        Bol("Good Evening")

    Bol("Jarvis here ,How may i help you Sir ?")
    
