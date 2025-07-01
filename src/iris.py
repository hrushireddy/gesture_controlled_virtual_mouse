import pyttsx3
import speech_recognition as sr
from datetime import date
import datetime
import time
import webbrowser
import sys
import requests
from threading import Thread
import app  # Assuming app.ChatBot is part of your framework
import random
import os
import pygetwindow as gw
import platform
import subprocess
import Gesture_Controller

# -------------Object Initialization---------------
today = date.today()
r = sr.Recognizer()  # Recognizer instance for speech recognition
engine = pyttsx3.init('sapi5')  # Initializing text-to-speech engine
voices = engine.getProperty('voices')  # Getting available voices
engine.setProperty('voice', voices[0].id)  # Setting the voice to use
is_awake = True  # Bot status, determines if the bot is active

# ------------------Functions----------------------
# Reply function for speaking out responses
def reply(audio):
    print(f"echo says: {audio}")  # Logging response to the console
    app.ChatBot.addAppMsg(audio)  # Add message to the chat interface
    engine.say(audio)  # Using pyttsx3 to speak the response
    engine.runAndWait()

# Function to greet the user based on the current time
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        reply("Good Morning!")
    elif 12 <= hour < 18:
        reply("Good Afternoon!")
    else:
        reply("Good Evening!")
    reply("I am iris, how may I assist you today?")

# Function to capture audio input from the user
def record_audio():
    with sr.Microphone() as source:
        print("Listening...")  # Debug message to indicate that the bot is listening
        r.pause_threshold = 0.8  # Adjusts sensitivity to pauses
        audio = r.listen(source, phrase_time_limit=5)  # Listen for input up to 5 seconds
        try:
            voice_data = r.recognize_google(audio)  # Convert speech to text using Google API
            
            print(f"Recognized: {voice_data}")  # Debug output to confirm recognition
            app.ChatBot.addUserMsg(voice_data)  # Add user message to the chat interface
        except sr.RequestError:
            reply('Sorry, the service is unavailable. Please check your Internet connection.')
            return ""
        
        except sr.UnknownValueError:
            
            print("Sorry, I did not understand that.")  # Debug message for unrecognized input
            return ""
        return voice_data.lower()  # Convert input to lowercase

def get_weather(city):
    api_key = 'd54dced93f3c87bde404f41683410856'  # Your API key
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(base_url)
    
    # Debug: print the raw response text from the API
    print(f"API Response Text: {response.text}")
    
    if response.status_code == 200:  # Successful API call
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        reply(f"The current weather in {city} is {weather_desc}. The temperature is {temp}°C, and it feels like {feels_like}°C.")
    else:
        reply("Sorry, I couldn't retrieve the weather information. Please check the city name or try again later.")

# Function to tell a joke using an online API
def tell_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:  # Successful response
        joke = response.json()
        reply(joke['setup'] + " ... " + joke['punchline'])
    else:
        reply("Sorry, I couldn't fetch a joke at the moment.")

def get_news():
    response = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2025-02-21&sortBy=publishedAt&apiKey=ce433e096a414e97a5f03add30819787&language=en")
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    
    if response.status_code == 200: 
        news = response.json()
        print(len(news["articles"]))
        print(random.randint(0, 99))
        a = random.randint(0, 99)
        reply(news["articles"][a]["title"] + "\n" + news["articles"][a]["description"])
    else:
        reply("Sorry, I couldn't fetch a news at the moment.")


def open_app(app_name):
    if app_name.lower() == "chrome":
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update path as necessary
        try:
            subprocess.run([chrome_path])
            reply("Opening Chrome.")
        except Exception as e:
            reply(f"Error opening Chrome: {e}")

    elif app_name.lower() == "microsoft edge":
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Edge path
        try:
            subprocess.run([edge_path])
            reply("Opening Microsoft Edge.")
        except Exception as e:
            reply(f"Error opening Microsoft Edge: {e}")

    elif app_name.lower() == "microsoft store":
        try:
            subprocess.run(["ms-windows-store:"])
            reply("Opening Microsoft Store.")
        except Exception as e:
            reply(f"Error opening Microsoft Store: {e}")

    elif app_name.lower() == "whatsapp":
        try:
            subprocess.run(["start", "whatsApp"], shell=True)
            reply("Opening WhatsApp.")
        except Exception as e:
            reply(f"Error opening WhatsApp: {e}")


import pyautogui

def respond(voice_data):
    global is_awake
    print(voice_data)

    if not is_awake:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    elif 'hello' in voice_data:
        wish()

    elif 'what is your name' in voice_data:
        reply("My name is iris.")
    
    elif 'date' in voice_data:
        reply(f"Today's date is {today.strftime('%B %d, %Y')}.")

    elif 'time' in voice_data:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        reply(f"The current time is {current_time}.")

    elif 'move left' in voice_data:
        pyautogui.moveRel(-100, 0)
        reply("Moving left.")

    elif 'move right' in voice_data:
        pyautogui.moveRel(100, 0)
        reply("Moving right.")

    elif 'move up' in voice_data:
        pyautogui.moveRel(0, -100)
        reply("Moving up.")

    elif 'move down' in voice_data:
        pyautogui.moveRel(0, 100)
        reply("Moving down.")

    elif 'click' in voice_data:
        pyautogui.click()
        reply("Clicking.")

    elif 'double tap' in voice_data:
        pyautogui.doubleClick()
        reply("Double tapping.")

    elif 'right click' in voice_data:
        pyautogui.rightClick()
        reply("Right clicking.")

    elif 'scroll up' in voice_data:
        pyautogui.scroll(100)
        reply("Scrolling up.")

    elif 'scroll down' in voice_data:
        pyautogui.scroll(-10)
        reply("Scrolling down.")

    elif 'top end' in voice_data:
        screen_width, screen_height = pyautogui.size()  # Get screen width and height
        pyautogui.moveTo(screen_width // 2, 0)  # Move the cursor to the top-center of the screen
        reply("Moving to the top.")

    elif 'bottom end' in voice_data:
        screen_width, screen_height = pyautogui.size()  # Get screen width and height
        pyautogui.moveTo(screen_width // 2, screen_height)  # Move the cursor to the bottom-center of the screen
        reply("Moving to the bottom.")

    elif 'left' in voice_data:
        screen_width, screen_height = pyautogui.size()  # Get screen width and height
        pyautogui.moveTo(0, screen_height // 2)  # Move the cursor to the left-center of the screen
        reply("Moving to the left.")

    elif 'right' in voice_data:
        screen_width, screen_height = pyautogui.size()  # Get screen width and height
        pyautogui.moveTo(screen_width, screen_height // 2)  # Move the cursor to the right-center of the screen
        reply("Moving to the right.")
    
    
    elif 'weather' in voice_data:
        reply("Please tell me the city.")
        city = record_audio()  # Capture the city name
        if city:
            get_weather(city)

    elif 'joke' in voice_data or 'tell me a joke' in voice_data:
        tell_joke()

    elif 'exit' in voice_data or 'terminate' in voice_data:
        reply("Shutting down. Goodbye!")
        sys.exit()
    
    elif 'news' in voice_data:
        get_news()
    
    elif 'search' in voice_data:
        query = voice_data.replace("search", "").strip()

        if query:
            reply(f"Searching for {query}.")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get().open(url)
            reply("Here is what I found.")
        else:
            reply("I didn't catch what you want to search for.")

    elif 'location' in voice_data:
        reply("Which place are you looking for?")
        place = record_audio()  # Capture the location name
        if place:
            url = f"https://www.google.com/maps/place/{place}"
            webbrowser.get().open(url)
            reply(f"Showing the location of {place} on Google Maps.")

    elif 'minimise window' in voice_data:
        try:
            # Minimize the active window
            active_window = gw.getActiveWindow()
            active_window.minimize()
            reply("Minimizing the window.")
        except Exception as e:
            reply(f"Error minimizing window: {e}")

    elif 'maximize window' in voice_data:
        try:
            # Minimize the active window
            active_window = gw.getActiveWindow()
            active_window.maximize()
            reply("Maximizing the window.")
        except Exception as e:
            reply(f"Error maximizing window: {e}")

    elif 'close this window' in voice_data:
        try:
            # Close the active window
            active_window = gw.getActiveWindow()
            active_window.close()
            reply("Closing the window.")
        except Exception as e:
            reply(f"Error closing window: {e}")
    elif 'minimise all windows' in voice_data:
        try:
            if platform.system() == 'Windows':
                pyautogui.hotkey('win', 'd')  # Windows shortcut to minimize all windows
                reply("Minimizing all windows.")
            elif platform.system() == 'Darwin':  # macOS
                pyautogui.hotkey('command', 'option', 'm')  # macOS shortcut to minimize all windows
                reply("Minimizing all windows.")
            else:
                reply("This feature is not supported on your operating system.")
        except Exception as e:
            reply(f"Error minimizing all windows: {e}")

    elif 'open' in voice_data:
        # Extract app name from the voice data after 'open'
        app_name = voice_data.split("open")[-1].strip()
        open_app(app_name)  # Call the open_app function
        
    elif 'bye' in voice_data or 'goodbye' in voice_data:
        reply("Goodbye! Have a great day.")
        is_awake = False
        sys.exit()

    elif 'launch gesture recognition' in voice_data:
        if Gesture_Controller.GestureController.gc_mode:
            reply('Gesture recognition is already active')
        else:
            gc = Gesture_Controller.GestureController()
            t = Thread(target = gc.start)
            t.start()
            reply('Launched Successfully')

    elif ('stop gesture recognition' in voice_data) or ('top gesture recognition' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
            reply('Gesture recognition stopped')
        else:
            reply('Gesture recognition is already inactive')

    else:
        reply("I'm sorry, I am not programmed to handle that command.")

# ------------------Driver Code--------------------

# Start the chatbot from the app module in a new thread
t1 = Thread(target=app.ChatBot.start)
t1.start()

# Wait for the chatbot to initialize
while not app.ChatBot.started:
    print("Waiting for ChatBot to start...")
    time.sleep(0.5)

# Greet the user when the bot is ready
wish()

# Main loop for continuous interaction
while True:
    voice_data = ""

    if app.ChatBot.isUserInput():
        voice_data = app.ChatBot.popUserInput()
        print(f"User input received: {voice_data}")

    if not voice_data:
        voice_data = record_audio()

    if voice_data:  # Process any recognized command
        try:
            respond(voice_data)
        except SystemExit:
            reply("Exit successful.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
