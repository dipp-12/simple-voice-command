
import speech_recognition as sr
import re
import webbrowser
import datetime

def greetings():
    print("Hello\n")
    currentH = int(datetime.datetime.now().hour)
    if currentH >=0 and currentH <12:
        print("Good Morning!\n")
    elif currentH >=12 and currentH <18:
        print("Good Afternoon!\n")
    else:
        print("Good Night!\n")

greetings()

def getCommand():
    r = sr.Recognizer()   

    with sr.Microphone() as source:
        print("Say something! I'm listening...\n")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + command + "\n")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio\n")
        command = getCommand()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return command.lower()


def runCommand(command):
    if 'hello' in command:
        print('Hello, How can I help you?')

    elif 'open google' in command:
        reg_ex = re.search('google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'where is this' in command:
        reg_ex = re.search('where (.*)', command)
        url = 'https://www.google.com/maps/@-7.1921691,109.6758026,9z'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        
    elif 'open website study' in command:
        reg_ex = re.search('web (.*)', command)
        url = 'https://igracias.ittelkom-pwt.ac.id/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open instagram' in command:
        reg_ex = re.search('web (.*)', command)
        url = 'https://www.instagram.com/ittelkompurwokerto/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')    
          
    elif 'thank you' in command:
            print('Goodbye!. Happy to help you. Have a good day.')
            exit()

    
#loop to continue executing multiple commands
while True:
    runCommand(getCommand())
    
