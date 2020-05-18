import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
from scraper import scraper
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
arr = ['pizza', 'burger', 'tacos', 'nachos', 'chinese',
       'Indian', 'fajitas', 'deserts', 'punjabi', 'North Indian']


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir, Did you Have Breakfast?")

    elif hour >= 12 and hour < 15:
        speak("Good Afternoon Sir, Did you Have Lunch?")

    else:
        speak("Good Evening Sir")

    speak("I'm Hazel , your new desktop assistant")


def takeCommand():
    """takes microphone input from
    user and returns output as a string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        """seconds on non speaking text before a text is considered complete"""
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print("user said :", query)
    except Exception as e:
        print(e)

        speak("I didn't quite get you, please say that again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amit.phaujdar@gmail.com', 'amitbikas')
    server.sendmail('amit.phaujdar@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'bye' in query:
            speak(
                "If you need me for anything else, I am right here Sir.Have a great day")
            break

        elif 'open tv shows' in query:
            speak("What would you like to see?")
            content1 = takeCommand()
            speak("What season would you like to view?")
            content2 = takeCommand()
            speak("What episode would you like to see?")
            content3 = takeCommand()
            content3 = int(content3)
            show_dir = r"C:\TV Shows"
            fin_show = show_dir + '\\' + content1 + '\\' + content2
            shows = os.listdir(fin_show)
            os.startfile(os.path.join(fin_show, shows[content3-1]))
        elif 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'i am hungry' in query:
            speak("What would you like to eat? Select an item")
            order = takeCommand()
            order = int(order)
            speak("You've ordered ")
            speak(arr[order-1])
            speak('can you confirm if this is infact your order?')
            confirm = takeCommand()
            if 'no' in confirm:
                continue
            elif 'yes' in confirm:
                speak('Showing results for your order nearby')
                url = "https://www.google.com/search?sxsrf=ALeKk01yfxqHPa8Y5NFPyslK2_aQg_IxMw:1589608402216&q="
                webbrowser.open(url+arr[order-1]+'+near+me')
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'find jobs' in query:
            speak("I can do that. What is your stipend threshold?")
            threshold = takeCommand()
            threshold = int(threshold)
            speak("Showing results for jobs you might like")
            scraper(threshold)
        elif 'how are you' in query:
            speak("I am doing just fine sir")
            speak("How about you sir?")
            content = takeCommand()
            if 'fine' in content:
                speak("That's great sir.What can I help you with? ")

            elif 'not good' in content:
                speak('Do you need a doctor?')
                command = takeCommand()
                if 'yes' in command:
                    speak('What kind of doctor do you need?')
                    command2 = takeCommand()
                    speak("Here's top doctors near you")
                    url = "https://www.google.com/search?sxsrf=ALeKk01yfxqHPa8Y5NFPyslK2_aQg_IxMw:1589608402216&q="
                    webbrowser.open(url+command2+'+near+me')
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'open my portfolio' in query:
            webbrowser.open("https://amitphaujdar.wixsite.com/portfolio")
        elif 'search on google' in query:
            speak("What should I search?")
            content = takeCommand()
            url = "https://www.google.com/search?sxsrf=ALeKk01yfxqHPa8Y5NFPyslK2_aQg_IxMw:1589608402216&q="
            webbrowser.open(url+content)
        elif 'search on youtube' in query:
            speak("What should I search?")
            content = takeCommand()
            url = "https://www.youtube.com/results?search_query="
            webbrowser.open(url+content)
        elif 'open music on saavn' in query:
            webbrowser.open(
                "https://www.jiosaavn.com/featured/weekly-top-songs/LdbVc1Z5i9E_")
        elif 'open Trello' in query:
            webbrowser.open("https://trello.com/")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The Time is ")
            speak(strTime)
        elif 'open wordpad' in query:
            path = r"C:\Program Files\Windows NT\Accessories\wordpad.exe"
            os.startfile(path)
        elif 'open visual studio code' in query:
            path = r"C:\Users\bikas\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)
        elif 'open pycharm' in query:
            path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.2\bin\pycharm64.exe"
            os.startfile(path)
        elif 'open android studio' in query:
            path = r"C:\Program Files\Android\Android Studio\bin\studio64.exe"
            os.startfile(path)

        elif 'open internshala' in query:
            webbrowser.open(
                "https://internshala.com/internships/matching-preferences")
        elif 'send email to amit' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = input()
                sendEmail(to, content)
                speak("Email has been sent sir")
            except Exception as e:
                print(e)
                speak("I'm sorry, the mail could not be sent. Please try again")
            # elif 'open music' in query:
            # logic for executing tasks is being written here based on query
