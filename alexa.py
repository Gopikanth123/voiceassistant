import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import smtplib
import wikipedia
import webbrowser as wb
from playsound import playsound
import pyautogui
import subprocess
import pywhatkit
from AppOpener import run
import json
import requests
import win32api
import randfacts
import bs4
import shutil 
from urllib.request import urlopen

engine=pyttsx3.init('sapi5')
engine.setProperty('rate',150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('volume',1)


def speak(str):
    engine.say(str)
    engine.runAndWait()



def wish():
    hour=int(datetime.datetime.now().hour)

    if 0<=hour<12:
        speak("good morning boss")
    elif hour>=12 and hour<16:
        speak("good afternoon boss")
    elif hour>=16 and hour<=21:
        speak("good evening boss")
    else:
        speak("good night boss")
    speak("waiting for your command")



def command():
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening....")
        r.pause_threshold=0.5
        audio=r.listen(mic,timeout=1,phrase_time_limit=5)
    try:
        print("Recognising....")
        text=r.recognize_google(audio,language='en-in')
        text=text.lower()
        print(text)
    except Exception as e:
        print("please say again")
        speak("something went wrong please say again boss")
        text="None"
    return text


def h():
    speak("enter the hour")
    try:
        ho=command()
        if ho.isnumeric()==False or len(ho)>2:
            h()
    except Exception as A:
        speak("please tell the hour again")
    return ho


def m():
    speak("enter the minutes")
    try:
        mi=command()
        if mi.isnumeric()==False or len(mi)>2:
            m()
    except Exception as B:
        speak("please tell the minutes again")
    return mi

def screenshot1():
    speak("screenshot will taken in 10 seconds")
    time.sleep(10)
    name=datetime.datetime.now()
    img_name=name.strftime('%Y%M%d%S%H%m')
    print("Img name= "+img_name)
    ti=img_name+".png"
    pyautogui.screenshot(ti)
    print('screenshot taken')
    speak('screenshot taken')

wishes={
    'are you single':"no i am in relationship with wifi",
    'what do you think about me':"kirrak",
    'how are you':"i am fine boss..  what about you boss",
    'fine':"It's good to know that your fine",
    'good':"It's good to know that your fine",
    "what's your name":"there is no name for me.. just i am assistant of gopi",
    'who made you':"I have been created by gopi.",
    'who is your god':"my boss! gopikanth.",
    'what are you doing':"waiting for your command",
    'what you will do in free time':"i always sleep while i am free",
}

apps={
    'open pycharm':"pyCharm community edition",
    'open whatsapp':"WhatsApp Beta",
    'open notepad':"notepad",
    'open chrome':"google chrome",
    'open edge':"Microsoft Edge",
    'open vs code':"Visual Studio Code",
    'open media player':"VLC media player",
    'open calculator':"calculator",
    'open word':"word",
    'open excel':"excel",
    'open powerpoint':"powerpoint",
    'open my sql':"mysql command line client - unicode",
    'open photos':"photos",
    'open mail':"mail",
    'open store':"Microsoft Store",
    'open calendar':"Calendar",
    'open adobe offers':"Adobe offers",
    'open vpn':"ExpressVPN",
    'open quick drop':"HP QuickDrop",
    'open settings':"Settings",
    'open 1 note':"OneNote",
    'open clock':"Clock",
    'open paint':"Paint",
    'open file manager':"File Explorer",
    'open tv':"Movies & TV",
    'open tips':"Tips",
    'open alexa':"Alexa",
    'open microsoft teams':"Microsoft Teams",
    'open command prompt':"Command Prompt",
    'open camera':"Camera",
    'open instagram':'Instagram',
    'open facebook':'Facebook'
}

domain=['search.in','search.com','search.net','search.edu','search.org','search.mil','search.gov']



url = "https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json"
response = urlopen(url)
data_json = json.loads(response.read())

if __name__=='__main__':
    wish()
    def run1():
        text=command().lower()
        text=text.lower()
        if "meaning of" in text:
            print(text)
            inp=text.replace("meaning of ","")
            try:
                print(data_json[inp])
                speak(data_json[inp])
                time.sleep(1)
            except Exception as D:
                speak("not found")
            
        elif "latest news" in text:
            speak('sure boss i will read it for you')
            #news_api=os.environ['news_api']
            news_api='7718679db5914d5b97d0903dddc201ea'
            print(news_api)
            com_api_link="https://newsapi.org/v2/top-headlines?country=in&At&apiKey="+news_api
            api_link=requests.get(com_api_link)
            api_data=api_link.json()
            #print(api_data)
            arr=[]
            try:
                for i in range(5):
                    arr.append(str(i+1)+". "+api_data["articles"][i]["title"]+".")
                for i in arr:
                    print(i)
                    speak(i)
                    time.sleep(1)
            except Exception as N:
                speak('exception occured')
        elif "weather" in text or "climate" in text or "rain" in text or "temperature" in text or "wind speed" in text or "humidity" in text:
            user_api=os.environ['my_api_key']
            print(user_api)
            speak("enter the city name")
            location=command().lower()
            complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
            api_link=requests.get(complete_api_link)
            api_data=api_link.json()
            if api_data['cod']=='404':
                print("Invalid city: {}, Please check the city name".format(location))
                speak("please check the city name boss")
                time.sleep(1)
            else:
                temp_city=((api_data['main']['temp'])-273.15)
                weather_desc=api_data['weather'][0]['description']
                hmdt=api_data['main']['humidity']
                wind_spd=api_data['wind']['speed']
                date_time=datetime.datetime.now().strftime("%d %b %y | %H:%M:%S")
                print("--------------------------------------------------------------")
                print("   weather stats for - {} || {}".format(location.upper(),date_time))
                print("---------------------------------------------------------------")
                print("   current temperature is: {:.2f} deg C".format(temp_city))
                speak("current temperature is "+str(temp_city)[6]+" degree Celsius")
                print("   current weather desc  :",weather_desc)
                speak("current weather description is "+weather_desc)
                print("   current wind speed is :",wind_spd,'kmph')
                speak('current wind speed is '+str(wind_spd)+' kmph')
                print("   current humidity is   :",hmdt,"%")
                speak('current humidity is '+str(hmdt)+' percentage')
                time.sleep(1)
        
        elif "fact" in text or "facts" in text:
            speak("sure boss")
            for i in range(3):
                x=randfacts.get_fact()
                print(x)
                speak(x)
            speak("hope you have satisfied")

        elif text in wishes:
            speak(wishes[text])
            time.sleep(1)
        elif "the time" in text:
            d=datetime.datetime.now().strftime("%H:%M")
            speak("the time is "+d)
        elif "play songs" in text:
            speak("playing")

            path=shutil.which('gallery')
            print(path)
            # songs=os.listdir(path)
            # print(songs)
            # os.startfile(os.path.join(path,songs[2]))
            time.sleep(1)
        elif 'play on youtube' in text:
            speak("what do you want to play")
            t=command().lower()
            pywhatkit.playonyt(t)
            time.sleep(10)
        # elif text in paths:
        #     text=text.replace("open ","")
        #     speak("opening "+text)
        #     text="open "+text
        #     os.startfile(paths[text])
        #     time.sleep(1)
        elif text in domain:
            speak("what do you want to search")
            te=command().lower()
            speak("opening "+te)
            #te=te.replace("open ","")
            text=text.replace("search","")
            te=te+text
            wb.open_new(te)
            time.sleep(1)
        elif text in apps:
            text=text.replace("open ","")
            speak("opening "+text)
            text="open "+text
            run(apps[text])
            time.sleep(1)
        elif "wikipedia" in text:
            speak("searching "+text)
            text=text.replace("wikipedia","")
            res=wikipedia.summary(text,sentences=1,auto_suggest=False)         
            print(res)
            speak(res)
            time.sleep(1)
        elif "screenshot" in text:
            speak('preparing for screenshot')
            screenshot1()
            time.sleep(1)
        # elif "send mail" in text:
        #     speak("what do you want to send boss")
        #     t=command().lower()
        #     speak(t)
        #     server=smtplib.SMTP('smtp.gmail.com',587)
        #     print("l1")
        #     server.starttls()
        #     print("l2")
        #     try:
        #         server.login('projectforpython32@gmail.com','Gopi@12345')
        #         print("----successfully login-----")
        #         server.sendmail('projectforpython32@gmail.com','gopikanthtirumani@gmail.com',t)
        #         print('mail sent')
        #         server.quit()
        #     except Exception as E:
        #         speak("oops something went wrong")
        #     time.sleep(1)
        # elif "send a whatsapp message" in text:
        #     speak("tell the mobile number")
        #     num=input("enter the mobile number:-\n")
        #     while len(num)!=10:
        #         num=input("enter the number again:-\n")
        #     num="+91"+num
        #     msg=command().lower()
        #     time_hour=int(input("enter the hour:-\n"))
        #     time_min=int(input("enter the minutes:-\n"))
        #     pywhatkit.sendwhatmsg(num,msg,time_hour,time_min)
        elif "set alarm" in text:
            speak("please tell me the timeto set alarm")
            hour=h()
            print(hour)
            min=m()
            print(min)
            t=hour+":"+min
            while True:
                if t==datetime.datetime.now().strftime("%H:%M"):
                    print("playing...")
                    try:
                        x=3700
                        y=300
                        for i in range(30):
                            win32api.Beep(x,y)
                            break
                    except Exception as e:
                        speak("exception occured")
            time.sleep(1)
        elif 'what' in text or 'who' in text or 'where' in text or 'how' in text or 'when' in text:
            url='https://www.google.com/search?q='+text
            header={
                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
            }
            request_result=requests.get(url)
            soup = bs4.BeautifulSoup(request_result.text,'html.parser').get_text()
            print(soup)
            speak(soup)
            time.sleep(3)

        elif ".in" in text:
            speak("opening "+text)
            text=text.replace("open ","")
            wb.open_new(text)
            time.sleep(1)
        elif ".com" in text:
            speak("opening "+text)
            text=text.replace("open ","")
            wb.open_new(text)
            time.sleep
        elif "open" in text:
            text=text.replace("open ","")
            speak("opening "+text)
            text=text+".com"
            wb.open_new(text)
            time.sleep(1)
        elif "thank you" in text:
            speak("see you boss")
            speak("have a good day")
            speak("take care")
            exit()
        else:
            speak("please say the command again")


while True:
    run1()
