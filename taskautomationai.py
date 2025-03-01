import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import openai
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

'''def sendEmail(content,to):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('saraswatnilesh3@gmail.com','your-password')
    server.sendemail('youremail@gmail.com',to,content)
    server.close()'''
       
if __name__ == '__main__':
    wishme()
    while 1: #while true for infinite time
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
        #elif "play song" in query:
            '''music_dir = "address"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))'''
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime(("%H:%M:%S"))
            speak(f"the time is :{strtime}")

        #f 'opencode' in query:
            #codepath="C:\Users\saras\OneDrive\Desktop\Visual Studio Code.lnk"
            #os.startfile(codepath)

      #elif 'email to nilesh' in query:
          #  try:
               # speak("what should i say?")
               # content = takecommand()
               #  to = "saraswatnilesh3@gmail.com"
             #    sendEmail(to,content)
            #     speak("email has been sent!")
         #    except Exception as e:
            #     print(e)
             #    speak("sorry my friend : i can't send email")'''


