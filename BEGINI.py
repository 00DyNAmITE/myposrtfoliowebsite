import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import time
import operator
import cv2
import requests
import wikipedia
import sys
import pyautogui 
import threading
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
import speedtest
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 150)

def calculator():
    speak("What operation would you like to perform? Addition, Subtraction, Multiplication, or Division?")
    operation = takeCommand().lower()    
    if operation in ["addition", "subtraction", "multiplication", "division"]:
        speak("enter the first number.")
        number1 = float(input(":"))
        speak("enter the second number.")
        number2 = float(input(":"))
        if operation == "addition":
            result = number1 + number2
        elif operation == "subtraction":
            result = number1 - number2
        elif operation == "multiplication":
            result = number1 * number2
        elif operation == "division":
            if number2 == 0:
                speak("Division by zero is not allowed.")
                return
            result = number1 / number2      
        speak(f"The result of {operation} of {number1} and {number2} is {result}")
    else:
        speak("Invalid operation.")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def relisteningcode():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("try again")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        hui = r.recognize_google(audio, language='en-us').lower()
        print(f"User said: {hui}\n")
    except sr.UnknownValueError:
        print("say again")
        return relisteningcode()
    except sr.RequestError:
        print("say again")
        return relisteningcode()
    if 'theory of general relativity' in hui:
        speak("BEGINI is activation please wait few seconds")
        time.sleep = 1
        speak("Activated")
    else:
        speak("wrong code")
        return relisteningcode()

def chatgpt():
    pyautogui.hotkey('ctrl', 'alt', 'k')
    time.sleep(3)
    pyautogui.moveTo(741,650,1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(763,611,1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write("chatgpt")
    pyautogui.hotkey('enter')
    pyautogui.moveTo(293, 431, 1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo('283', '136', '1')
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo('913', '1012', '1')
    pyautogui.click()
    query = query.replace("chat gpt", "").strip()
    pyautogui.write(f"{query}")
    pyautogui.hotkey('enter')

def login():
    speak("who are you?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us').lower()
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return login()
    except sr.RequestError:
        print("Couldn't request results from Google Speech Recognition. Please check your internet connection.")
        return login()
    
    if 'sun is about to go down' in query:
        return None
    elif 'shaurya' in query:
        speak("helloo shourya bansal")
        speak("tell code to activate BEGINI")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            hui = r.recognize_google(audio, language='en-us').lower()
            print(f"User said: {hui}\n")
        except sr.UnknownValueError:
            print("say again")
            return relisteningcode()
        except sr.RequestError:
            print("say again")
            return relisteningcode()
        if 'theory of general relativity' in hui:
            speak("BEGINI is activating please wait few seconds")
            time.sleep(1)
            speak("Activated")
            return None
        else:
            speak("wrong code")
            return login()
    else:
        speak("okk")
        speak("tell code to activate BEGINI")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            hui = r.recognize_google(audio, language='en-us').lower()
            print(f"User said: {hui}\n")
        except sr.UnknownValueError:
            print("say again")
            return relisteningcode()
        except sr.RequestError:
            print("say again")
            return relisteningcode()
        if 'theory of general relativity' in hui:
            speak("BEGINI is activating please wait few seconds")
            time.sleep(1)
            speak("Activated")
            return None
        else:
            speak("wrong code")
            return login()

def tell_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke_data = response.json()
        speak(f"Here's a joke for you: {joke_data['setup']} ... {joke_data['punchline']}")
    except Exception as e:
        speak("I couldn't fetch a joke right now.")

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning Sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon Sir.")
    else:
        speak("Good evening Sir.")
    speak("Ready for your help. What can I do?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us').lower()
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return "None"
    except sr.RequestError:
        print("Couldn't request results from Google Speech Recognition. Please check your internet connection.")
        return "None"
    return query

def openMinecraft():
    minecraft_path = r"C:\Users\shour\OneDrive\Desktop\TLauncher.lnk"
    if os.path.exists(minecraft_path):
        speak("Opening Minecraft.")
        try:
            os.startfile(minecraft_path)
        except OSError:
            speak("Error opening Minecraft. Please check the application path.")
    else:
        speak("Sorry, I couldn't find Minecraft on your desktop.")

def open_application(application_path):
    if os.path.exists(application_path):
        try:
            os.startfile(application_path)
            speak(f"Opening {os.path.basename(application_path)}.")
        except OSError:
            speak(f"Error opening {os.path.basename(application_path)}. Please check the application path.")
    else:
        speak(f"Sorry, I couldn't find {os.path.basename(application_path)} on your system.")

def openmspaint():
    mspaint_path = r"C:\Users\shour\OneDrive\Desktop\mspaint.lnk"
    if os.path.exists(mspaint_path):
        speak("Opening paint.")
        try:
            os.startfile(mspaint_path)
        except OSError:
            speak("Error opening mspaint. Please check the application path.")
    else:
        speak("Sorry, I couldn't find paint on your desktop.")

def searchGoogle(query):
    speak(f"Searching Google for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def searchYouTube(query):
    speak(f"Searching YouTube for {query}")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def play_video_in_loop(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def create_folder_and_file():
    folder_path = r"C:\Users\shour\OneDrive\Desktop\BIGINItextfiles"
    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder: {e}")
        return None
    file_number = 1
    while True:
        file_name = f"textfile{file_number}.txt"
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            break
        file_number += 1
    return file_path

def game_guess_number():
    speak("Welcome to the Guess the Number game!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        speak("Guess a number between 1 and 100.")
        guess = int(input(": "))
        attempts += 1
        if guess < number:
            speak("Too low!")
        elif guess > number:
            speak("Too high!")
        else:
            speak(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def game_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    speak("Let's play Rock, Paper, Scissors.")
    while True:
        speak("Your turn: rock, paper, or scissors?")
        user_choice = takeCommand().lower()
        if user_choice not in choices:
            speak("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        ai_choice = random.choice(choices)
        speak(f"I chose {ai_choice}.")
        if user_choice == ai_choice:
            speak("It's a tie!")
        elif (user_choice == "rock" and ai_choice == "scissors") or (user_choice == "paper" and ai_choice == "rock") or (user_choice == "scissors" and ai_choice == "paper"):
            speak("You win!")
        else:
            speak("I win!")
        speak("Do you want to play again? Yes or No?")
        if "no" in takeCommand().lower():
            break

def game_quiz_level_hard():
    questions = {
        "what nothingness called in the language of science?": "dark matter",
        "what is the particle of gravity?": "graviton",
        "what is the name of that event that started universe": "big bang"

    }
    score = 0
    speak("Welcome to the Quiz Game!")
    for question, answer in questions.items():
        speak(question)
        user_answer = takeCommand().lower()
        if user_answer == answer:
            speak("Correct!")
            score += 1
        else:
            speak(f"Wrong! The correct answer is {answer}.")
    speak(f"Your final score is {score} out of {len(questions)}.")

def game_quiz_level_medium():
    questions = {
        "which articles is removed from kashmir": "arcticle 370",
        "what is the particle of light": "photons",
        "how many type of particles present in one atom": "3"

    }
    score = 0
    speak("Welcome to the Quiz Game!")
    for question, answer in questions.items():
        speak(question)
        user_answer = takeCommand().lower()
        if user_answer == answer:
            speak("Correct!")
            score += 1
        else:
            speak(f"Wrong! The correct answer is {answer}.")
    speak(f"Your final score is {score} out of {len(questions)}.")

def game_quiz_level_easy():
    questions = {
        "how much time was taken to wrote an india constitution?": "2years 11months 18days",
        "who discovered the value of infinity?": "ramanujan",
        "who ia god of cricket": "sachin tendulkar"

    }
    score = 0
    speak("Welcome to the Quiz Game!")
    for question, answer in questions.items():
        speak(question)
        user_answer = takeCommand().lower()
        if user_answer == answer:
            speak("Correct!")
            score += 1
        else:
            speak(f"Wrong! The correct answer is {answer}.")
    speak(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    login()
    video_thread = threading.Thread(target=play_video_in_loop, args=(r'C:\Users\shour\OneDrive\Pictures\Saved Pictures\VN20240524_120350.mp4',))
    video_thread.start()
    time.sleep(1)
    speak ("INTRODUCING my self")
    speak ("BEGINI")
    speak ("An artificial inteligence")

    wishme()
    while True:
        query = takeCommand()

        if 'begini' in query: #1
            print("Yes, Sir?")
            speak("Yes, Sir?")

        elif 'who are you' in query :#2
            speak("My name is BEGINI. I can do everything that my creator programmed me to.")

        elif 'who created you' in query:#3
            print("Shourya Bansal")
            speak("Shourya Bansal")

        elif 'just open google' in query:#4
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif 'open google' in query: #5
            speak("What should I search?")
            qwe = takeCommand()
            searchGoogle(qwe)

        elif 'just open youtube' in query:#6
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'open youtube' in query:#7
            speak("What would you like to watch?")
            qwer = takeCommand().lower()
            searchYouTube(qwer)

        elif 'open minecraft' in query:#8
            openMinecraft()

        elif 'find' in query:#9
            search_query = query.split('find', 1)[1].strip()
            searchGoogle(search_query)

        elif 'search on youtube' in query:#10
            query = query.replace("search on youtube", "").strip()
            searchYouTube(query)

        elif 'close browser' in query:#11
            speak("Closing browser.")
            os.system("taskkill /f /im msedge.exe")

        elif 'close chrome' in query:#12
            speak("Closing Chrome.")
            os.system("taskkill /f /im chrome.exe")

        elif 'open paint' in query:#13
            openmspaint()

        elif 'close paint' in query:#14
            speak("Closing paint.")
            os.system("taskkill /f /im mspaint.exe")

        elif 'open wordpad' in query:#15
            path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Wordpad.lnk"
            os.startfile(path)

        elif 'close wordpad' in query:#16
            speak("Closing Wordpad.")
            os.system("taskkill /f /im wordpad.exe")

        elif 'open powerpoint' in query:#17
            path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(path)

        elif 'close powerpoint' in query:#18
            speak("Closing PowerPoint.")
            os.system("taskkill /f /im POWERPNT.exe")

        elif 'open ms word' in query:#19
            path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(path)

        elif 'close ms word' in query:#20
            speak("Closing MS Word.")
            os.system("taskkill /f /im WINWORD.exe")

        elif 'open command' in query:#21
            os.system("start cmd")

        elif "close command" in query:#22
            speak("Closing command prompt.")
            os.system("taskkill /f /im cmd.exe")

        elif 'play music' in query:#23
            music_dir = r'C:\playlist'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'close music' in query:#24
            speak("Stopping music.")
            os.system("taskkill /f /im vlc.exe")

        elif 'what is the time' in query or 'what is time' in query:#25
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif "shutdown pc" in query:#26
            speak("Shutting down PC.")
            os.system("shutdown /s /t 1")

        elif "restart pc" in query:#27
            speak("Restarting PC.")
            os.system("shutdown /r /t 1")

        elif 'lock pc' in query:#28
            speak("Locking PC.")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif 'what is my ip address' in query:#29
            speak("Checking.")
            try:
                ipAddn = requests.get('https://api.ipify.org').text
                print(ipAddn)
                speak(f"Your IP address is {ipAddn}")
            except Exception as e:
                speak("Network is weak, please try again later.")

        elif 'start typing' in query:#30
            speak("Starting typing mode. I will log everything you say into a text file.")
            text_file_path = create_folder_and_file()
            if text_file_path:
                speak("You can start speaking. Say 'stop typing' to finish.")
                typed_text = []
                while True:
                    speech = takeCommand()
                    if 'stop typing' in speech:
                        speak("Stopping typing mode. Text saved.")
                        with open(text_file_path, 'w') as file:
                            file.write('\n'.join(typed_text) + '\n')
                        speak("Opening the file.")
                        os.startfile(text_file_path)
                        break
                    typed_text.append(speech)

        elif 'what is' in query or 'who is' in query:#19
            try:
                person = query.replace('what is', '').replace('who is', '').strip()
                info = wikipedia.summary(person, sentences=2)
                print(info)
                speak(f"according to wikipedia {info} ")
            except wikipedia.exceptions.DisambiguationError:
                speak(f"There are multiple results for {person}. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak(f"I couldn't find any information on {person}. Please try another query.")

        elif 'open camera' in query:#33
            pyautogui.hotkey('ctrl', 'alt', 'c')

        elif 'go to sleep' in query:#34
            speak(' alrigth sir i am switching off now')
            sys.exit()

        elif 'take screenshot' in query:#35
            speak("tell me a name for file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif 'volume up' in query:#36
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif 'volume down' in query:#37
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif 'mute' in query:#38
            pyautogui.press("volumemute")

        elif 'unmute' in query:#39
            pyautogui.press("volumemute")
       
        elif 'draw a line' in query:#40
            time.sleep(2)
            start_x = 321
            start_y = 465
            end_x = 910
            end_y = 465
            pyautogui.moveTo(start_x, start_y)
            pyautogui.mouseDown()
            pyautogui.moveTo(end_x, end_y, duration=0.5)  
            pyautogui.mouseUp()
        elif 'draw a square' in query:#41
            pyautogui.moveTo(x=1000, y=300 ,duration=1)
            pyautogui.leftClick
            distance = 400
            pyautogui.click()
            pyautogui.dragRel(distance, 0, duration=1)
            pyautogui.dragRel(0, distance, duration=1)
            pyautogui.dragRel(-distance, 0, duration=1)
            pyautogui.dragRel(0, -distance, duration=1)

        elif 'red colour' in query:#42
            pyautogui.moveTo(x=1125, y=115, duration=1)
            pyautogui.click(x=1125, y=115, clicks=1, interval=0, button='left')

        elif 'draw a rectangular spiral' in query:#43
            start_x = 321
            start_y = 465
            initial_distance = 300
            pyautogui.moveTo(start_x, start_y)
            pyautogui.mouseDown()
            distance = initial_distance
            while distance > 0:
                pyautogui.dragRel(distance, 0, 0.1, button='left')  
                distance -= 10
                pyautogui.dragRel(0, distance, 0.1, button='left')   
                pyautogui.dragRel(-distance, 0, 0.1, button='left')   
                distance -= 10
                pyautogui.dragRel(0, -distance, 0.1, button='left')   
            pyautogui.mouseUp()
            print("Rectangular spiral drawn.")

        elif 'bigini select all' in query:#44
            speak("okk sir")
            pyautogui.hotkey('ctrl', 'a')

        elif 'select all' in query:#45
            pyautogui.hotkey('ctrl', 'a')

        elif 'bold' in query:#46
            pyautogui.hotkey('ctrl', 'b')

        elif 'copy' in query:#47
            pyautogui.hotkey('ctrl', 'c')

        elif 'replace' in query:#48
            pyautogui.hotkey('ctrl', 'h')

        elif 'italic' in query:#49
            pyautogui.hotkey('ctrl', 'i')

        elif 'open downloads' in query:#50
            pyautogui.hotkey('ctrl', 'j')

        elif 'new' in query:#51
            pyautogui.hotkey('ctrl', 'n')

        elif 'open' in query:#52
            pyautogui.hotkey('ctrl', 'o')

        elif 'print' in query:#53
            pyautogui.hotkey('ctrl', 'p')
        
        elif 'save it' in query:#54
            pyautogui.hotkey('ctrl', 's')

        elif 'underline' in query:#55
            pyautogui.hotkey('ctrl', 'u')

        elif 'paste' in query:#56
            pyautogui.hotkey('ctrl', 'v')

        elif 'cut' in query:#57
            pyautogui.hotkey('ctrl', 'x')

        elif 'redo' in query:#58
            pyautogui.hotkey('ctrl', 'y')

        elif 'undo' in query:#59
            pyautogui.hotkey('ctrl', 'z')

        elif 'switch to recent tab' in query:#60
            pyautogui.hotkey('alt', 'tab')
        
        elif 'hu r u' in query:#61
            speak("Well I am bigini the voice artificial intelligence voice assistant")
            speak("i can do everything that shourya programmed me to do")

        elif 'what r u' in query:#62
            speak("Well I am bigini the voice artificial intelligence voice assistant")
            speak("i can do everything that shourya programmed me to do")

        elif 'what are you' in query:#63
            speak("Well I am bigini the voice ai voice assistant")
            speak("i can do everything that shourya programmed me to do")

        elif 'tell me about shaurya' in query:#64
            speak("HE is my creator a 14 year old boy who is learning coding")

        elif 'play song' in query:#65
            pyautogui.hotkey('ctrl','alt','s')
            time.sleep(9)
            pyautogui.moveTo(952,418,1 )
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1250, 370,1 )
            pyautogui.click()
            time.sleep(1)
            query = query.replace("play song", "").strip()
            pyautogui.write(f"{query}")
            pyautogui.hotkey('enter')
            time.sleep(1)
            pyautogui.moveTo(1544, 770, 1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1455, 766, 1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1793,301,1)
            pyautogui.click()
        
        elif 'locate my cursor' in query:#66
            hui = pyautogui.position()
            speak(hui)

        elif 'tell joke' in query:#67
            tell_joke()

        elif 'calculator' in query:#68
            calculator()

        elif 'chat gpt' in query:#69
            pyautogui.hotkey('ctrl', 'alt', 'k')
            time.sleep(3)
            pyautogui.moveTo(741,650,1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(930, 549, 1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.write("chatgpt")
            pyautogui.hotkey('enter')
            pyautogui.moveTo(305, 374, 1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(281, 131, 1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(913, 1012,1)
            pyautogui.click()
            query = query.replace("chat gpt", "").strip()
            pyautogui.write(f"{query}")
            pyautogui.hotkey('enter')

        elif "send mail" in query:#70
            speak ("whom you want to send e-mail")
            koo = input(":")
            speak ("what is your subject?")
            hupi = takeCommand()
            speak ("what do you want to send in mail?")
            jikl = takeCommand()
            pyautogui.hotkey('ctrl', 'alt', 'm')
            time.sleep(10)
            pyautogui.moveTo(140, 125, 1)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(999, 268, 1)
            pyautogui.click()
            pyautogui.write(koo)
            pyautogui.hotkey('tab')
            pyautogui.write(hupi)
            pyautogui.hotkey('tab')
            pyautogui.write(jikl)
            pyautogui.moveTo(856, 188, 1)
            pyautogui.click()

        elif 'i want information from number' in query:#71
            speak("please enter the number")
            num = input(":")
            number = num
            pepnumber = phonenumbers.parse(number)
            location = geocoder.description_for_number(pepnumber, "en")
            service_pro = carrier.name_for_number(pepnumber, "en")
            print(location)            
            print(service_pro)
            speak(f"his country name is {location}")            
            speak(f"and company name of his phone number is {service_pro}")

        elif 'i want to play games' in query:#72
            speak("which game you want to play")
            speak("you can play quiz, rock paper scissors and number guess ")
            game = takeCommand()
            if 'quiz' in game:
                speak("which level sir")
                speak("easy, medium, hard")
                level = takeCommand()
                speak("okay, let's play quiz")
                if 'easy' in level:
                    game_quiz_level_easy()
                elif 'medium' in query:
                    game_quiz_level_medium()
                else:
                    game_quiz_level_hard()

            elif 'rock paper scissor' in game:
                speak("okay, let's play rock paper scissor")
                game_rock_paper_scissors()

            elif 'number guess' in game or 'number gas' in game:
                speak("okay, let's play number quiz")
                game_guess_number()

        elif 'exit' in query or 'stop' in query:
            speak("Take care of yourself.")
            speak("Goodbye Sir")
            break
    