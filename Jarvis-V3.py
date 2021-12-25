import pyttsx3   # pip install pyttsx3 == text data into speach using python
import datetime  # default module function
import speech_recognition as sr # pip install speechRecognition == speech from mic to text format
import smtplib  # default module function
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui  # pip install pyautogui
import webbrowser as wb
from time import sleep
import wikipedia  # pip install wikipedia
import pywhatkit    # pip install pywhatkit
import requests
from newsapi import NewsApiClient    # pip install newsapi
                                     # pip install newsapi-python  to solve the dependency error

import clipboard    # pip install clipboard 
import os   # default module
import pyjokes #pip install pyjokes
import time as tt
import random
import psutil    #pip install psutil




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine .say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak("Hello sir, I am jarvis version 3.0 ")

    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        speak("Hello sir, I am Friday version 3.0 ")

     

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # hour =I minutes=M seconds=S 
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening Sir!") 
    else:
        speak("Good night Sir!")

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    greeting()
    speak("Jarvis at your service, please tell me how can I assist you?")     

# while True:
#     voice = int(input("Press 1 for male voice::\nPress 2 for female voice\n"))
#     speak(audio) 

#     getvoices(voice)
# wishme()

def takeCommandCMD():
    query =input("please tell me how can I assist you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....") 
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio , language="en-IN")
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again Please....")
        return "None"
    return query 

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


def sendwhatsmsg(phone_no, message):
    Message = message 
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    search = takeCommandMic()
    speak('what should I search for?') 
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key ='0db73378193d47b38735789a9e82fd37')
    speak('what topic you need the news about?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q = topic,
                                    language='en',
                                    page_size=5)

    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}')) 
        
    speak("that is for now I will update you in some time")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]}\n Deaths :{data["deaths"]}\n Recovered {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\Hp\\Desktop\\Jarvis-V3\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()



def flip():
    speak("okay sir, flipping a coin")
    coin = ['heads','tales']
    toss = [] 
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("I flipped the coin and you got"+toss)


def roll():
    speak("okay sir, rolling a dice for you") 
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("I roll a die and you got"+roll)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)
    battery =psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)         

                                             



    


if __name__ == "__main__":

    getvoices(1)
    wishme()
    while True:
        query = takeCommandMic().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date() 

        elif 'email' in query:
            email_list = {
                'test email':'josephfrancizz009@gmail.com , mca531@rajagiri.edu'
            }
            try:
                speak("To whom you want to send the mail?")
                name = takeCommandMic()
                receiver = email_list[name]
                speak("What is the subect of the mail?")
                subject = takeCommandMic()
                speak('What should I say?')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak("email has been send")

            except Exception  as e:
                print(e)
                speak("unable to send the  email")

        elif 'message' in query:
            user_name = {
                
                'Jarvis': '+91 9447620966'
            }

            try:
                speak("To whom you want to send the whats app message?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("What is the message?")
                message = takeCommandMic()
                sendwhatsmsg(phone_no, message)
                speak("Message has been send")

            except Exception  as e:
                print(e)
                speak("unable to send the  Message")

        elif 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'search' in query:
            searchgoogle() 

        elif 'youtube' in query:
            speak("what should I search for on youtube?")
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)

        elif 'weather' in query:
            city = 'ernakulam'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=a0bc9a06ec372ced8ef38dd6f8f457a0'

            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data ['weather'] [0] ['description']
            temp = round((temp - 32)* 5/9)  # this formula converts from fahrenheit to degree celsius
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} city is like')
            speak('Temperature is : {} degree celsius'.format(temp))
            speak('Weatheris {}'.format(desp))

        elif 'news' in query:
            news()


        elif 'read' in query:
            text2speech()


        elif 'covid' in query:
            covid()

        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('open','')))    

        elif 'open code' in query:
            codepath = 'C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe' 
            os.startfile(codepath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif 'screenshot' in query:
            screenshot()


        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = 'D:\Songs'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))    
            

        elif 'remember' in query:
            speak("what should I remember?")
            data = takeCommandMic()
            speak("you said to me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close() 


        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you told me to remember thar "+remember.read()) 

        elif 'flip' in query:
            flip() 

        elif 'roll' in query:
            roll() 


        elif 'cpu' in query:
            cpu()
                                             

        elif 'offline' in query:
            quit()
                


