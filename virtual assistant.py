
# IMPORT REQUIRED MODULES

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib
import pywhatkit as kt
import random
import pyperclip

#SETUP THE VOICE OF THE MACHINE 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' ,voices[0].id)

# FUNCITON TO SPEAK THE INPUT TEXT

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# FUNCTION TO GREAT

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Sir")
    elif (hour>=12 and hour <= 18):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("How may i help you!")

# FUNCTION TO TAKE THE COMMANDS FROM THE USER

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening your commands .....")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing your command .....")
        query = r.recognize_google(audio,language='en-in')
        print(f"Command Recieved --- {query}\n")
    
    except Exception as e:
        speak("Say that again please !")
        return "None"
    return query

# FUNCTION TO SEND THE EMAIL FROM THE GIVEN ID

emails= {}
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('email-id' , 'password')
    server.sendmail('email-id' , to , content)
    server.close()

# FUNCTION TO ADD EMAIL IN THE DICTIONARY

def add_email():
    speak("Enter the nick name of the person in the terminal ")
    key = input("nick name = ")
    speak("Enter the email id of the person in the terminal ")
    email = input("email id = ")
    emails[key] = email

# ALL THE FUNCTIONALITY 

def basic_functions():
    
    while True:    

# TAKE THE INPUT FROM THE USER 

        query = takeCommand().lower()

# PERFORM THE TASK AS PER THE INPUT 

    # SEARCH THE CONTENT IN WIKIPEDIA

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query,sentences = 3)
            speak("According to wikipedia")
            speak(results)

    #  READ THE SELECTED TEXT (COPY THE TEXT TO THE CLIPBOARD)
        
        elif 'read the text' in query:
            text = pyperclip.copy()
            speak(str(text))

    # OPEN YOUTUBE IN THE DEFAULT BROWSER

        elif ('start youtube'in query) or( 'open youtube' in query):
            webbrowser.open("youtube.com")

    # OPEN GOOGLE IN THE DEFAULT BROWSER

        elif ('start google'in query) or ('open google' in query):
            webbrowser.open("google.com")

    # OPEN GOOGLE CLASSROOM IN THE DEFAULT BROWSER

        elif ('start google classroom'in query) or ('open google classroom' in query):
            webbrowser.open("classroom.google.com")

    # OPEN STACKOVERFLOW IN THE DEFAULT BROWSER

        elif ('start stackoverflow'in query) or ('open stackoverflow' in query):
            webbrowser.open("stackoverflow.com")

    # TELL THE TIME

        elif 'the time' in query:
            Time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {Time}")

    # OPEN THE GIVEN CODE EDITOR

        elif 'open code editor' in query:
            path = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

    # PLAY THE MUSIC IN GIVEN DIRECTORY

        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Music'
            songs = os.listdir(music_dir)   
            try:                    
                os.startfile(os.path.join(music_dir, songs[random.randint(len(songs))]))
            except Exception as e:
                speak("No Music records found in the folder!")
        
    # ADD EMAIL ID
        
        elif ("add email")in query:
            add_email()

    # SEND EMAIL

        elif 'send email ' in query:
            for name in query[query.index("email")+1 : ]:
                if name in emails.keys():
                    to = emails[name]
                else:
                    speak("No email id found saved by that name ")
            try:
                speak("What is the content of email?")
                content = takeCommand()
                sendEmail(to,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("There is some problem in sending the email!")

    # GOOGLE SEARCH THE STATEMENT PROVIDED IN COMMAND

        elif ('web search' in query) or ('google search' in query):
            index = query.index('search')
            target = query[index+1:]
            kt.search(target)

    # EXIT THE CODE

        elif ('exit the program' in query) or ('exit this program' in query) or ('take rest' in query) or ('quit program' in query):
            break
    
if __name__ == "__main__":
    wish()
    basic_functions()
