import pyttsx3  #pip install pyttsx3.this module used for text to speach
import datetime
import speech_recognition as sr #pip install SpeechRecognition.without internate connection SpeechRecognition canot work
import wikipedia # pip install wikipedia
import smtplib #this for email
import webbrowser as wb #searching
import os #it is for logout,shutdown,restart
import pyautogui #pip install pyautogui. it is for screenshot
import psutil #it is use for cpu,battery percentage.pip install psutil
import pyjokes #pip install pyjokes.it is jokes
+


#<---------------------coding text to speach part starting------------------------>

engine=pyttsx3.init()   #it will call intial function of pyttsx3 module. engine is a variable

def speak(audio):
    engine.say(audio)  # say() is  a predefine funtion it will convert text to speach
    engine.runAndWait()  # runAndwait() fuction will wait till it finish speaking

#speak("this is jarvis ai assistant")

#<-------------coding of text to speach part ending------------------------------>

#<----------------------------starting date+ time function coding---------------------------------->

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #it will give us current time
    speak("the current time is")
    speak(Time)
#time()

def date():
    year=int(datetime.datetime.now().year)                      #it will give us current year
    month=int(datetime.datetime.now().month)                    #it will give us current month
    day=int(datetime.datetime.now().day)                         #it will give us current day
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
#date()
#<--------- -----------------ending date+ time function coding----------------------------------------------->


#<--------- -----------------starting wishme() function coding----------------------------------------------->
def wishme():
    speak("Wellcome back sir!")
    time()  #calling time function
    date() #calling date function
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        speak("Good evening sir!")
    else:
        speak("Good night sir")
    speak("jarvis at your service please tell me how can i help you?")
#wishme() #calling wishme() function

#<--------- -----------------ending wishme() function coding----------------------------------------------->

#<--------- -----------------start voice recognize function coding----------------------------------------------->

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening....")
        r.pause_threshold=1 #after opening jarvis it will wait 1 second then starting listening
        audio=r.listen(source)#listening the users audio
    try:
            print("Recongnizing.....")
            query=r.recognize_google(audio, language='en-in') #users audio will be recognize by google and store to the query
            print(query)
    except Exception as e:
            print(e)
            speak("said that again please ")
            return "None"
    return query
#takeCommand()

#<--------- -----------------ending voice recognize function coding----------------------------------------------->
def sendEmail(to,content): #sendemai has two parametar ->we use to for email adress and content use for email detail
    server=smtplib.SMTP('smtp.gmail.com',587) #this is our gmail adresss smtp.gmail.com and gmail port 587
    server.ehlo()
    server.starttls()
    server.login('abarik172018@gmail.com','123')
    server.sendmail('abarik172018@gmail.com',to,content)
    server.close()
#<------------------------------starting coding of screenshot function------------------------------->
def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\HP\\PycharmProjects\\Minor_project\\ss.png")
#<---------------------------------Ending coding of screenshot function----------------------------------->
#<---------------------------------starting coding of jokes function------------------------------------>
def jokes():
    speak(pyjokes.get_joke())

#<-----------------------------ending coding of jokes function--------------------------->
#<------------------------start coding of  cpu update--------------------------------------------------->
def cpu():
    usage=str(psutil.cpu_percent())
    speak('cpu is at'+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


#<--------- ----------------- ending coding of cpu function----------------------------------------------->


#<--------- ----------------- starting coding of main function----------------------------------------------->

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower() # taking all command in lower case
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'search in chrome' in query:
            speak('what should i search?')
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search =takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s/t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play song' in query:
            songs_dir='E:\\bengali music'
            songs= os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'listen' in query:
            speak("what should i remembar?")
            data= takeCommand()
            speak("you said me to remembar that"+data)
            remembar=open('data.txt','w')
            remembar.write(data)
            remembar.close()
        elif 'do you know anything' in query:
            remembar=open('data.txt','r')
            speak("you said to me remember that"+remembar.read())

        elif 'cpu' in query:
            cpu()

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to='xyz@gmail.com'  #recivers gmail address
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("unable to sent email!")
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'joke' in query:
            jokes()

        elif 'offline' in query:  #if i say offline then program will stop
            quit()

#<--------- ----------------- ending coding of main function----------------------------------------------->
