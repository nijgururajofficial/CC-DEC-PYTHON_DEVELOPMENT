import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour > 12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am alexa, how may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
        
    
    except Exception as e:
        print("Please say again..")
        return "None"
    
    return query

def run_alexa():
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching in Wikipedia")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            speak(results)
        
        elif "day" in query:
            day = datetime.datetime.now().strftime('%A')
            speak(f"It is {day}")

        elif "time" in query:
            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            ampm = "AM" if hour < 12 else "PM"
            time = f"{hour} {min} {ampm}"
            speak(time)

        elif "open youtube" in query:
            webbrowser.open_new_tab("https://youtube.com")
        
        elif "open google" in query:
            webbrowser.open_new_tab("https://google.com")
        
        elif "play" in query:
            song = query.replace('play','')
            speak('playing'+song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            key = query.replace('search','')
            speak(f'searching {key} on google')
            pywhatkit.search(key)
        
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif "exit" in query:
            speak("Amigos")
            break
        
        elif 'siri' in query:
            speak("Don't ever talk to me again")
            break

if __name__ == "__main__":
    wishMe()
    run_alexa() 
    
            
