import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
       speak("Good Morning Sir !")

    elif hour>=12 and hour<18:
       speak("Good Afternoon sir!")

    elif hour>=18 and hour<20 :
        speak("Good Evening sir!")

    else :
        speak("Good Night sir !")

speak("Hello Sir ,I am Jarvis . Please tell me how may I help you ? ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("Listening .......")
     r.pause_threshold = 1
     audio = r.listen(source ,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing .....")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said: {query}\n")  
    
    except Exception as e:
        #print(e)

        print("Say that again please....")
        return "None "
    return query



if __name__ == '__main__':
    wishMe()
    while True :
    #if 1 :
        query= takeCommand().lower()


        if 'wikipedia' in query:

            speak("Searching wikipedia ...")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According To wikipedia")
            speak(results) 
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com") 
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverfflow.com")      

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            #print(songs)    
            os.startfile(os.path.join(music_dir, songs[9]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , The time is : {strTime} ")
        elif 'open code ' in query :
            codePath = "C:\\Users\\AMEYA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        


         