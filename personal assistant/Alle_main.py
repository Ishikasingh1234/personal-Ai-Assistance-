import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import os

for i in range(3):
    a = input("Enter Password to open AllE :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [Wake up] ")
        break
    elif (i==2 and a!=pw):
        exit()
    elif (a!=pw):
        print("Try Again")

# ******************************************





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)
print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 
                
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how r u" in query:
                    speak("Perfect, sir")
                elif "thank u" in query:
                    speak("you are welcome, sir")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "weather in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")

                elif "news" in query:
                    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"xml")
                    news = data.find_all("item")
                    for i in range(5):
                        title = news[i].title.text
                        speak(title)


                elif "open notepad" in query:
                    os.startfile("notepad.exe")
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\91914\\OneDrive\\Desktop\\personal assistant\\FocusMode.py")
                        exit()
                    else:
                        pass
