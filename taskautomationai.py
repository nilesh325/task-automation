import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices) to know no. of voices available in system
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir .please tell me how i can help you")

def takecommand():
    '''takes input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("lisentening.....")
        r.pause_threshold = 1#time after which if you don't speak then code with excute by default it's 
        audio = r.listen(source)

    try:
        print("recongnizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said :{query}\n")

    except Exception as e:
        print(e)
        print("say that again please")
        return "None"

    return query
    
if __name__ == '__main__':
    wishme()
    while true: #while true for infinite time
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime(("%H:%M:%S"))
            speak(f"the time is :{strtime}")
            


