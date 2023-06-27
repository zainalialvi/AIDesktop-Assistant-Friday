import webbrowser
import speech_recognition as sr
from openaiTest import AI
import os
from soundsData import sounds
from sitesData import sites
from appData import apps
from TimeData import dateAndTime
from chatbot import chat
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    print(f"Text is: {text}")
    speaker.speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 4000
        print("Listening...")
        audio = r.listen(source, timeout=5)
        try:
            command = r.recognize_google(audio, language="en-US")
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")

    return ""  # Return an empty string if no valid response was received within the timeout


if __name__ == '__main__':
    print("Hello i am Friday. How may I help you..! ")
    while True:
        print("----------------------------------------")
        query = takeCommand()
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say("opening site sir")
                webbrowser.open(site[1])

        for sound in sounds:
            if f"play {sound[0]}".lower() in query.lower():
                say("Playing sound sir")
                os.startfile(sound[1])

        for app in apps:
            if f"open {app[0]}".lower() in query.lower():
                os.startfile(app[1])

        if "time".lower() in query.lower():
            say(f"Time is: {dateAndTime}")

        elif f"AI".lower() in query.lower():
            AI(query)

        elif "bye".lower() in query.lower():
            say("Okay bye.")
            exit()

        else:
            ai_answer = chat(query)
            say(ai_answer)
