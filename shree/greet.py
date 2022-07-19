def wishMe(self):
    hour = int(datetime.now().hour)
    if hour >= 0 and hour <= 12:
        self.speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        self.speak("Good Afternoon")
    else:
        self.speak("Good Evening")

    self.speak("Jarvis here ,How may i help you Sir ?")
