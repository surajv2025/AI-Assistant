import sys
import pyaudiowpatch
sys.modules["pyaudio"] = pyaudiowpatch   # pehle ye

import speech_recognition as sr   

def speech_to_text():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        
        voice_data=""
        voice_data=r.recognize_google(audio)
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:    
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, I could not request results from Google Speech Recognition service.")
        
        
        
        
if __name__ == "__main__":
    speech_to_text()
    