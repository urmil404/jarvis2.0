import pyttsx3

def Bol(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print("    ")
    print(f"JARVIS==>{Text}")
    engine.say(Text)
    engine.runAndWait()
    print(" ")


if __name__=="__main__":
    Bol("Hello Sir")
