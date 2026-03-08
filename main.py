# import speech_recognition as sr
# import webbrowser
# import pyttsx3 

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait() 

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")    
#     elif "open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
        
    
        
# if __name__ == "__main__":
#     speak("Initializing Jarvis...")

#     while True:
#             # listen for wake word "jarvis"
#         r = sr.Recognizer()
        

#         # recognize speech using Sphinx
#         print("recognizing....")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening!!!")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "jarvis"):
#                  speak("yaa")
#                  #listen for command
#                  with sr.Microphone() as source:
#                      print("jarvis Active...")
#                      audio = r.listen(source)
#                      command = r.recognize_google(audio)
                     
#                      processCommand(command)
        
#         except Exception as e:
#             print("Sphinx error; {0}".format(e))  




import speech_recognition as sr
import webbrowser
import pyttsx3 


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait() 

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")    
    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    else:
        speak("Sorry, I didn't understand that command.")
     
        
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)   
                print("Listening for wake word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)  

            word = r.recognize_google(audio)
            print(f"Heard: {word}")   

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)  # 🔧
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)  
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")   
                    processCommand(command)
        
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Google API error: {e}")
        except Exception as e:
            print(f"Error: {e}")