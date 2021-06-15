import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import random
import socket
import wikipedia
import  webbrowser
import pywhatkit as kit
import smtplib
from constants import Constant as const
import  sys
import pyjokes
import pyautogui




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#To convert voice into text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query



#to wish
def wish():
    date = datetime.datetime.now()
    hour = int(date.hour)
    hour_in_12 = hour
    if(hour_in_12 > 12):
        hour_in_12 -= 12
    time = f"{hour_in_12}:{date.minute}"
    if hour>=0  and hour<=12:
         speak(f"good morning, its:{time}")
    elif hour>12 and hour<18:
        speak(f"good afternoon, its:{time}")
    else:
        speak(f"good evening, right now time is: {time}")
    speak("i am jarvis sir, please tell me how can i help you")

#to send email
def sendEmail (to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(const.from_mail, const.from_password)
    server.sendmail(const.from_mail, to, content)
    server.close()

#for news updates
def news():
    main_url = f"{const.news_url}{const.new_url_api_key}"
    main_page = get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")






if __name__ == "__main__":
    notepad_path = "C:\\WINDOWS\\system32\\notepad.exe"
    paint_path = "C:\\WINDOWS\\system32\\mspaint.exe"
    wish()
    flag = True
    while flag:
        query = take_command().lower()
        # logic building for tasks
        if 'open notepad' in query:
            os.startfile(notepad_path)
        elif "open paint" in query:
            os.startfile(paint_path)
        elif "close code" in query:
            flag = False
        elif "open camera" in query:
         cap = cv2.VideoCapture(0)
         while True:
             ret, img = cap.read()
         cv2.imshow('webcam', img)
         k = cv2.waitKey(50)
         if k==27:
             break
         cap.release()
         cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "F:\\rahul\\rudra\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
        # elif "stop music" in query:
        #     os.system("taskkill /f /im Groove Music")
        elif "ip address" in query:
            url = 'codespeedy.com'
            # ip = get(url).text
            ip = socket.gethostbyname(url)
            speak(f"your internet home address is {ip}")
        elif "wikipedia" in query:
            speak("searching  wikipedia...")
            query = query.replace("wikipedia","")
            results =  wikipedia.summary(query, sentences=2)
            speak("according to  wikipedia")
            speak(results)
           # print(results)
        elif"open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = take_command().lower()
            webbrowser.open(f"https://www.google.com/search?q={hundar}")
        elif "open free fire" in query:
            webbrowser.open("www.garena free fire.com")
        elif "send message" in query:
            kit.sendwhatmsg("+918394931742")
        elif "play video on youtube" in query:
            speak("sir, which video should i play on youtube")
            vid_name = take_command().lower()
            kit.playonyt(f"{vid_name}")
        elif "play song on youtube" in query:
            speak("sir, which song should i play on youtube")
            vid_name = take_command().lower()
            kit.playonyt(f"{vid_name}")
        elif "email to me" in query:
            try:
                speak("what should i say?")
                content = take_command().lower()
                to = const.to_mail
                sendEmail(to, content)
                speak("Email has been sent!!")

            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to sent this mail!!")
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit(1)

        #to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().minute)
            if nn == 38:
                music_dir = "F:\\rahul\\rudra\\songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        #to find a jokes
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(f"Hi Sir, {joke}")
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()


        speak("sir, do you have any other work")





