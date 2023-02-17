import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init("sapi5")
voices =engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        r.energy_threshold= 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said-{query}")

    except Exception as e:
        print("...Say That Again...")
        return "None"
    return query 
    
if __name__== "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep " in query:
                    speak("ok sir, please call me anytime when you were in need ")
                    break

                elif "hello" in query :
                    speak (" hello sir, how are you ?")
                elif "i am fine" in query:
                    speak ("that's great ")
                elif "how are you" in query:
                    speak ("i am also good sir")
                elif "thank you" in query:
                    speak("you are welcome sir")
                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in aligarh"
                    url =f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in aligarh"
                    url =f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")    








