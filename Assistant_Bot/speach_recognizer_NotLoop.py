from cgitb import text
from email.mime import audio
from js2py import require
import speech_recognition 
import pyttsx3
import time

answer = 'No software yet'

def Get_Time(required):
    now = time.gmtime()
     
    required_time = f"{now[3]+3}:{now[4]}"
    required_date = f"{now[2]}/{now[1]}/{now[0]}"

    if required == "date":
        return required_date
    
    elif required == 'time':
        return required_time

def open_google():
    pass

def Input():
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        
        recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
        audio = recognizer.listen(mic)
        said = ''
        try:
            said = recognizer.recognize_google(audio)
            said = said.lower()
            
            print(f"reconnized \n{said}")

            

        except speech_recognition.UnknownValueError:
            print("error")
    return said

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

'''text = Input()
#text = "good morning"x
speak(text)'''

#need a function to ditect the required
required = "time"
print(Get_Time(required))