import pyttsx3  #pip install pyttsx3(text to speech module)
import speech_recognition as sr  #pip install speechRecognition  
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup 
import time

print("Installing SHREE")

MASTER = "Shradha" 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#speak fncn will pronounce the string which is passed to it...
def speak(text):
    engine.say(text)
    engine.runAndWait()
    

#this fncn will wish as per the current time  
def wishMe():    
    hour = int(datetime.datetime.now().hour)   
    #print(hour)
    if hour>= 0 and hour< 12:
        speak("GOOD MORNING" + MASTER)

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON" + MASTER)
    
    else:
        speak("GOOD EVENING" + MASTER)

    speak("I am SHREE . How May I help you..?")


#this fncn will take command from the microphone
def takeCommand():
    #the Recognizer class
    r = sr.Recognizer()
    with sr.Microphone() as source:
            r.pause_threshold=1 #seconds of non-speaking before a phrase is considered complete
            print("Listening...")
            audio = r.listen(source)   
            
    try:
            print("Recognizing...")
            #method for recognizing speech from an audio source
            query = r.recognize_google(audio , language='en-in')
            print(f"user said : {query}\n") #f - string interpolation tool , format string...

    except Exception as e:
            print("Say  that again please!")
            query = None
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)  
    server.ehlo()
    server.starttls()
    server.login('Csestudents461@gmail.com','thinkfriday')
    server.sendmail('shradhagupta21@gmail.com' , to , content)
    server.close()

#main prgrm starts here...
if __name__ == "__main__":
   speak("Installing Shree")
   wishMe()
while True:
    query = takeCommand()

    #logic for executing tasks as per the query...
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query , sentences = 2)
        print(results)
        speak(results)

    elif "open youtube" in query.lower():
        url="youtube.com"
        #chrome_path = 'C:\Program Files\Google\Chrome\Application %s'
        webbrowser.open(url)

    elif "open google" in query.lower():
        url="google.com"
        webbrowser.open(url)

    elif "play music" in query:
        songs=os.listdir("C:\\Users\\HP\\Music")
        print(songs)

    elif "the time" in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif "open code" in query.lower():
        codePath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif "open stack overflow" in query.lower():
        webbrowser.open("https://stackoverflow.com/")
    
    elif 'email to shraddha' in query.lower():
        try:
         speak("What should I send?")
         content = takeCommand()
         to = "shradhagupta211@gmail.com"
         sendEmail(to,content)
         speak("Email has been sent successfully")

        except Exception as e:
            print(e)

    elif 'temperature' in query.lower():
         search = "temperature in Shimla"
         url = f"https://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         temp = data.find("div",class_="BNeawe").text
         speak(f"current{search} is {temp}")

    elif "who are you" in query.lower():
        speak("I am your desktop assistant created by Shradha")

    elif "don't listen" in query.lower():
        speak("for how much time you want to stop Shree from listening commands")
        a = int(takeCommand())
        time.sleep(a)
        print(a)

    elif "exit" in query.lower():
         speak("Thanks for giving me your time")
         exit()

    
        









