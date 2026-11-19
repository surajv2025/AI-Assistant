import text_to_speech
 
import  datetime
import webbrowser
import weather

def Action(data):
    user_input =  data.lower()

    if "name" in user_input or "who are you" in user_input:
        text_to_speech.text_to_speech("My name is virtual assistant.")
        return "My name is virtual assistant"
    elif"hello" in user_input:
         text_to_speech.text_to_speech("Hello, how are you?")
         return "Hello, how are you?"
    elif "good morning" in user_input:
         text_to_speech.text_to_speech("Good morning, have a nice day!")
         return "Good morning, have a nice day!"
    elif"time" in user_input:
        now = datetime.datetime.now().strftime("%I:%M %p").lstrip("0")
        reply = f"The time is {now}"
        text_to_speech.text_to_speech(reply)
        return reply
    
    elif "shutdown" in user_input:
         text_to_speech.text_to_speech("Ok sir.")
         return "Ok sir."

    elif "play music" in user_input:
         webbrowser.open("https://www.youtube.com/watch?v=3JZ_D3ELwOQ")
         text_to_speech.text_to_speech("Ok sir, playing music for you.")
         return "Ok sir, playing music for you."
    elif "open google" in user_input:
         webbrowser.open("https://www.google.com")
         text_to_speech.text_to_speech("Ok sir, opening Google for you.")
         return "Ok sir, opening Google for you."
    elif "open youtube" in user_input:
         webbrowser.open("https://www.youtube.com")
         text_to_speech.text_to_speech("Ok sir, opening YouTube for you.")  
         return "Ok sir, opening YouTube for you."
    elif "weather" in user_input or "mausam" in user_input:
        # Call the weather API and get the current weather information
        weather_info = weather.weather()
        text_to_speech.text_to_speech(f"The current weather is {weather_info}.")
        return f"The current weather is {weather_info}."
    else:
         text_to_speech.text_to_speech("Sorry, I did not understand that.")   
    
    
 
      
    
    