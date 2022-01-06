import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pyjokes
import random
import requests
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

## speak("Dont Buy Alexa! Build Your own using Python")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Python: Listening...")
        audio=r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"You: {query}")
            return query
        except:
            print("Try again")
    ##return query

while True:
    #input user command as a lower case string to be read
    query = command().lower() 

    if 'name' in query:
        speak("Hello Sean! My name is Jarvis")
    elif 'are you single' in query:
        answers = ['I am a robot', 'I cannot comprehend Human relationships']
        speak(random.choice(answers))

    elif 'hate' in query:
        speak("I hate being called Alexa or Google, I am Jarvis!")

    elif 'love' in query:
        speak("I love helping you friend!")

    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("It's " +time+" Friend")

    elif 'joke' in query:
        joke = pyjokes.get_joke()
        speak(joke)
        speak("Was that funny friend?")
        reply = str(command().lower())
        if reply == 'yes' or reply == 'yeah':
            speak("Glad I could make you laugh friend")
        elif reply == 'no' or reply == 'nope':
            speak("I guess I'll have to do better next time, Sorry friend")
            pass
    elif 'who is' in query:
        query = query.replace('who is', "")
        speak(wikipedia.summary(query,2))

    elif 'search' in query:
        query = query.replace('search',"")
        webbrowser.open_new_tab(query)

    elif 'bye' in query:
        speak("Have a nice day!")
        break
    else:
        speak("What are you talking about?")


print(command())

