import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia

class speakAudio:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voices',voices[0].id)
    def speak(self,audio):
        self.engine.say(audio)
        print(audio)
        self.engine.runAndWait()
    
    def takeCommand(self):
        r = sr.Recognizer()
        # with mic as source:
        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 15000
            r.pause_threshold = 1
            self.speak("Listening...")
            audio = r.listen(source)
            print("Listening...")

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said : {query}\n")

        except Exception as e:
            # print(e)
            print("say that again please...")
            self.speak("say that again please...")
            return "None"
        return query

class Greetings(speakAudio):
    def wishMe(self):
        hour = int(datetime.now().hour)
        if hour >= 0 and hour <= 12:
            self.speak("Good Morning")
        elif hour >= 12 and hour <= 18:
            self.speak("Good Afternoon")
        else:
            self.speak("Good Evening")

        self.speak("Jarvis here ,How may i help you Sir ?")


if __name__=="__main__":
    audio = speakAudio()
    greet = Greetings()
    greet.wishMe()


