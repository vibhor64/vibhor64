import pyttsx3
import datetime
from pywhatkit.main import take_screenshot
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from datetime import date
import urllib.request
import re
import pywhatkit as kit
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import requests
import yfinance as yf

# get-StartApps

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)



def speak(audio):

    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Omen. How may I assist you?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.dynamic_energy_ratio = 5
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        # query = r.recognize_google(audio, Language='en-in')
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Voice not recognized. Please speak again.")
        return "none"
    return query

def pricee():
                query = takeCommand().upper()
                query= query.replace(" ", "")
                msft = yf.Ticker(f"{query}")
                if msft.info['regularMarketPrice'] == None:
                    print(f"Share not recognized please try again")
                    speak(f"Share not recognized please try again")
                    pricee()
                else:
                    print(f"{msft.info['regularMarketPrice']} dollars per share")
                    speak(f"{msft.info['regularMarketPrice']} dollars per share")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        try:

            if 'omen' in query:
                query = query.replace("omen", "")



            if query == 'goodbye':
                speak("goodbye, have a nice day!")
                exit()

            if query == 'bye':
                speak("goodbye, see you soon!")
                exit()

            if query == 'fuck off':
                speak("have a nice day!")
                exit()

            if query == 'shut up':
                speak("goodbye!")
                exit()

            if query == 'exit':
                speak("Good day, see you later!")
                exit()

            if 'make to do' in query:
                file1 = open("ToDoList.txt", "w")
                speak('Writing a to-do list...')
                print('Writing a to-do list...')
                query = takeCommand().lower()
                file1.write(f"\n To-Do List\n {query}")
                speak("Your to-do list has been created")
                print("Your to-do list has been created")
                file1.close()
            
            if 'read to do' in query:
                file1 = open("ToDoList.txt", "r")
                print(file1.read())
                readtodo = file1.read()
                speak(readtodo)




            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences = 2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)
            

        
            elif 'open youtube' in query:
                speak("Opening YouTube...")
                print("Opening YouTube...")
                searchResult = (f"https://www.youtube.com")
                webbrowser.open(f"{searchResult}")

            elif 'open google' in query:
                speak("Opening Google...")
                print("Opening Google...")
                searchResult = (f"https://www.google.com")
                webbrowser.open(f"{searchResult}")

            elif 'open amazon' in query:
                speak("Opening Amazon...")
                print("Opening Amazon...")
                searchResult = (f"https://www.amazon.in")
                webbrowser.open(f"{searchResult}")

            elif 'open reddit' in query:
                speak("Opening Reddit...")
                print("Opening Reddit...")
                searchResult = (f"https://www.reddit.com")
                webbrowser.open(f"{searchResult}")
            
            elif 'open github' in query:
                speak("Opening Git Hub...")
                print("Opening GitHub...")
                searchResult = (f"https://www.github.com")
                webbrowser.open(f"{searchResult}")
            
            elif 'open instagram' in query:
                speak("Opening Instagram...")
                print("Opening Instagram...")
                searchResult = (f"https://www.instagram.com")
                webbrowser.open(f"{searchResult}")
            
            elif 'open twitch' in query:
                speak("Opening Twitch...")
                print("Opening Twitch...")
                searchResult = (f"https://www.twitch.com")
                webbrowser.open(f"{searchResult}")
            
            elif 'open facebook' in query:
                speak("Opening Facebook...")
                print("Opening Facebook...")
                searchResult = (f"https://www.facebook.com")
                webbrowser.open(f"{searchResult}")
            
            elif 'open twitter' in query:
                speak("Opening Twitter...")
                print("Opening Twitter...")
                searchResult = (f"https://www.twitter.com")
                webbrowser.open(f"{searchResult}")
            
            elif 'open pintrest' in query:
                speak("Opening Pintrest...")
                print("Opening Pintrest...")
                searchResult = (f"https://www.pintrest.com")
                webbrowser.open(f"{searchResult}")

            elif 'open website ' in query:
                query = query.replace("open website ", "")
                speak(f"Opening {query}...")
                print(f"Opening {query}...")
                query = query.replace(" ", "+")
                searchResult = (f"https://www.{query}.com")
                webbrowser.open(f"{searchResult}")



            elif 'what' and 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"The time is {strTime}")

            elif 'what' and 'day' in query:
                current_time = datetime.datetime.now() 
                day = current_time.day
                if day == 1 or day == 21 or day == 31:
                    day = (f"{day}st")
                elif day == 2 or day == 22:
                    day = (f"{day}nd")
                elif day == 3 or day == 23:
                    day = (f"{day}rd")
                else:
                    day = (f"{day}th")
                month = current_time.month
                if month == 1:
                    print(f"Today is {day} of January, ", end="")
                    speak(f"Today is {day} of January, ", end="")
                if month == 2:
                    print(f"Today is {day} of February, ", end="")
                    speak(f"Today is {day} of February, ", end="")
                if month == 3:
                    print(f"Today is {day} of March, ", end="")
                    speak(f"Today is {day} of March, ", end="")
                if month == 4:
                    print(f"Today is {day} of April, ", end="")
                    speak(f"Today is {day} of April, ", end="")
                if month == 5:
                    print(f"Today is {day} of May, ", end="")
                    speak(f"Today is {day} of May, ", end="")
                if month == 6:
                    print(f"Today is {day} of June, ", end="")
                    speak(f"Today is {day} of June, ", end="")
                if month == 7:
                    print(f"Today is {day} of July, ", end="")
                    speak(f"Today is {day} of July, ")
                if month == 8:
                    print(f"Today is {day} of August, ", end="")
                    speak(f"Today is {day} of August, ", end="")
                if month == 9:
                    print(f"Today is {day} of September, ", end="")
                    speak(f"Today is {day} of September, ", end="")
                if month == 10:
                    print(f"Today is {day} of October, ", end="")
                    speak(f"Today is {day} of October, ", end="")
                if month == 11:
                    print(f"Today is {day} of November, ", end="")
                    speak(f"Today is {day} of November, ", end="")
                if month == 12:
                    print(f"Today is {day} of December, ", end="")
                    speak(f"Today is {day} of December, ", end="")
                dayrn = datetime.datetime.now()
                print(dayrn.strftime("%A"))


            elif 'news' in query:
                query_params = {
	            "source": "bbc-news",
	            "sortBy": "top",
	            "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
	            } 
                main_url = " https://newsapi.org/v1/articles"

	            # fetching data in json format
                res = requests.get(main_url, params=query_params)
                open_bbc_page = res.json()

	            # getting all articles in a string article
                article = open_bbc_page["articles"]

	            # empty list which will
	            # contain all trending news
                results = []

                for ar in article:
	                results.append(ar["title"])

                for i in range(len(results)):
	                print(i + 1, results[i])
                speak(results)

            #Open Opera Gx Browser
            elif 'opera' in query:
                speak(f"Opening Opera...")
                print(f"Opening Opera...")
                opPath = "C:\\Users\\mukes\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
                os.startfile(opPath)

            #Open VS Code
            elif 'code' in query:
                speak(f"Opening VS Code...")
                print(f"Opening VS Code...")
                codePath = "C:\\Users\\mukes\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'Netflix' in query:
                speak(f"Opening Netflix...")
                print(f"Opening Netflix...")
                codePath = "Netflix.exe"
                os.startfile(codePath)
            
            if 'discord' in query:
	            speak("Opening Discord...")
	            print("Opening Discord...")
	            os.system('start shell:appsfolder\com.squirrel.Discord.Discord') 
            
            elif 'powershell' in query:
                speak(f"Opening Power Shell...")
                print(f"Opening Powershell...")
                codePath = "Powershell.exe"
                os.startfile(codePath)
            
            elif 'photoshop' in query:
                speak(f"Opening Adobe Photoshop...")
                print(f"Opening Adobe Photoshop...")
                codePath = "Photoshop.exe"
                os.startfile(codePath)
            
            elif 'illustrator' in query:
                speak(f"Opening Adobe Illustrator...")
                print(f"Opening Adobe Illustrator...")
                codePath = "Illustrator.exe"
                os.startfile(codePath)
            
            elif 'in design' in query:
                speak(f"Opening Adobe Indesign...")
                print(f"Opening Adobe Indesign...")
                codePath = "Indesign.exe"
                os.startfile(codePath)

            elif 'open spotify' in query:
                speak(f"Opening Spotify...")
                print(f"Opening Spotify...")
                codePath = "Spotify.exe"
                os.startfile(codePath)

            elif 'light room' in query:
                speak(f"Opening Adobe Lightroom...")
                print(f"Opening Adobe Lightroom...")
                codePath = "Lightroom.exe"
                os.startfile(codePath)
            
            elif 'steam' in query:
                speak(f"Opening Steam...")
                print(f"Opening Steam...")
                codePath = "steam.exe"
                os.startfile(codePath)
            
            elif 'excel' in query:
                speak(f"Opening Excel...")
                print(f"Opening Excel...")
                codePath = "Excel.exe"
                os.startfile(codePath)

            elif 'open zoom' in query:
                speak(f"Opening Zoom...")
                print(f"Opening Zoom...")
                codePath = "Zoom.exe"
                os.startfile(codePath)
            
            elif 'open word' in query:
                speak(f"Opening Word...")
                print(f"Opening Word...")
                codePath = "winword.exe"
                os.startfile(codePath)
            
            elif 'open teams' in query:
                speak(f"Opening Microsoft Teams...")
                print(f"Opening Microsoft Teams...")
                codePath = "Teams.exe"
                os.startfile(codePath)
            
            if 'skype' in query:
	            speak("Setting up Skype...")
	            print("Setting up Skype...")
	            os.system('start shell:appsfolder\Microsoft.SkypeApp_kzf8qxf38zg5c!App') 

            if 'maps' in query:
	            speak("Opening Maps...")
	            print("Opening Maps...")
	            os.system('start shell:appsfolder\Microsoft.WindowsMaps_8wekyb3d8bbwe!App') 
            
        
            if 'amazon prime' in query:
	            speak("Opening Amazon Prime Video...")
	            print("Opening Amazon Prime Video...")
	            os.system('start shell:appsfolder\AmazonVideo.PrimeVideo_pwbj9vvecjh7j!App') 
            
            if 'calculator' in query:
	            speak("Opening Calculator...")
	            print("Opening Calculator...")
	            os.system('start shell:appsfolder\Microsoft.WindowsCalculator_8wekyb3d8bbwe!App') 

                


            if 'alarm' in query:
	            speak("Setting up Alarm...")
	            print("Setting up Alarm...")
	            os.system('start shell:appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App') 
            
            if 'check weather' in query:
	            speak("Checking weather...")
	            print("Checking weather...")
	            os.system('start shell:appsfolder\Microsoft.BingWeather_8wekyb3d8bbwe!App') 

            if 'check traffic' in query:
	            print("Checking traffic...")
	            speak("Checking traffic...")
	            os.system('start shell:appsfolder\Microsoft.WindowsMaps_8wekyb3d8bbwe!App') 
            
        

            elif 'open settings' in query:
                speak(f"Opening Settings...")
                print(f"Opening Settings...")
                os.system('start shell:appsfolder\windows.immersivecontrolpanel_cw5n1h2txyewy!microsoft.windows.immersivecontrolpanel') 
                

            elif 'chrome' in query:
                speak(f"Opening chrome...")
                print(f"Opening chrome...")
                codePath = "%PROGRAMFILES(x86)%\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codePath)

            
            elif 'search youtube' in query:
                speak("Searching on youtube...")
                print("Searching on YouTube...")
                query = query.replace("search youtube ", "")
                query = query.replace(" ", "+")
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
                vidId = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                video = (f"https://www.youtube.com/watch?v={vidId[0]}")
                webbrowser.open(f"{video}")
            
            elif 'search on youtube' in query:
                speak("Searching on youtube...")
                print("Searching on YouTube....")
                query = query.replace("search on youtube ", "")
                query = query.replace(" ", "+")
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
                vidId = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                video = (f"https://www.youtube.com/watch?v={vidId[0]}")
                webbrowser.open(f"{video}")

            elif 'youtube search' in query:
                speak("Searching on youtube...")
                print("Searching on YouTube....")
                query = query.replace("youtube search ", "")
                query = query.replace(" ", "+")
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
                vidId = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                video = (f"https://www.youtube.com/watch?v={vidId[0]}")
                webbrowser.open(f"{video}")

            elif 'play ' and 'on youtube ' in query:
                speak("Playing your song now...")
                print("Playing your song now...")
                query = query.replace("on youtube ", "")
                query = query.replace("play ", "")
                query = query.replace(" ", "+")
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
                vidId = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                video = (f"https://www.youtube.com/watch?v={vidId[0]}")
                webbrowser.open(f"{video}")
            
            elif 'play ' and 'in youtube ' in query:
                speak("Playing your song now...")
                print("Playing your song now...")
                query = query.replace("in youtube ", "")
                query = query.replace("play ", "")
                query = query.replace(" ", "+")
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
                vidId = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                video = (f"https://www.youtube.com/watch?v={vidId[0]}")
                webbrowser.open(f"{video}")
            
            elif 'search google' in query:
                speak("Searching on Google...")
                print("Searching on Google....")
                query = query.replace("search google ", "")
                query = query.replace(" ", "+")
                searchResult = (f"https://www.google.com/search?q={query}")
                webbrowser.open(f"{searchResult}")
            
            elif 'search on google' in query:
                speak("Searching on Google...")
                print("Searching on Google....")
                query = query.replace("search on google ", "")
                query = query.replace(" ", "+")
                searchResult = (f"https://www.google.com/search?q={query}")
                webbrowser.open(f"{searchResult}")

            elif 'google search' in query:
                speak("Searching on Google...")
                print("Searching on Google....")
                query = query.replace("google search ", "")
                query = query.replace(" ", "+")
                searchResult = (f"https://www.google.com/search?q={query}")
                webbrowser.open(f"{searchResult}")

            elif 'play' and 'on spotify' in query:
                speak("Playing your song now...")
                print("Playing your song now...")
                query = query.replace("play", "")
                query = query.replace("on spotify", "")
                query = query.replace(" ", "%20")
                # html = urllib.request.urlopen(f"https://open.spotify.com/search/{query}")
                # playerId = re.findall(r"track/(\S{47})", html.read().decode())
                # song = (f"https://www.youtube.com/watch?v={playerId[0]}")
                webbrowser.open(f"https://open.spotify.com/search/{query}")
            
            
            elif 'bitcoin' in query:
                response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
                data = response.json()
                price = data["bpi"]["USD"]["rate"]
                print(f"Bitcoin is priced at {price} dollars per coin")
                speak(f"Bitcoin is priced at {price} dollars per coin")

            elif 'stock' in query:
                print('Which stock price do you want? (in NASDAQ)')
                speak('Which stock price do you want? (in NASDAQ)')
                pricee()
                
            
            
                


            elif "send what's app message" in query:
                query = query.replace("send what's app message", "")
                num = input("Whom do you want to send message to (phone number with country code)? ")
                speak("Whom do you want to send message to (phone number with country code)? ")
                kit.sendwhatmsg_instantly(f"{num}", "{query}", 20)

            elif "send WhatsApp message" in query:
                query = query.replace("send WhatsApp message", "")
                num = input("Whom do you want to send message to (phone number with country code)? ")
                speak("Whom do you want to send message to (phone number with country code)? ")
                kit.sendwhatmsg_instantly(f"{num}", "{query}", 20)

            elif "screenshot" in query:
                speak("Taking screenshot...")
                print("Taking screenshot...")
                take_screenshot()

            elif "screen shot" in query:
                speak("Taking screenshot...")
                print("Taking screenshot...")
                take_screenshot()

            elif "close tab" in query:
                print("Closing tab...")
                speak("Closing tab")
                kit.close_tab()
                
            elif "mute" in query:
                print("Your system has been muted")
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                # Get current volume 
                currentVolumeDb = volume.GetMasterVolumeLevel()
                # volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
                # # NOTE: -6.0 dB = half volume !
                volume.SetMute(1, None)

            elif "reduce volume" in query:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                # Get current volume 
                currentVolumeDb = volume.GetMasterVolumeLevel()
                volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
                # # NOTE: -6.0 dB = half volume !
                speak("System volume has been reduced")
                print("System volume has been reduced")

            elif "decrease volume" in query:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                # Get current volume 
                currentVolumeDb = volume.GetMasterVolumeLevel()
                volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
                # # NOTE: -6.0 dB = half volume !
                speak("System volume has been reduced")
                print("System volume has been reduced")

            elif "increase volume" in query:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                # Get current volume 
                currentVolumeDb = volume.GetMasterVolumeLevel()
                volume.SetMasterVolumeLevel(currentVolumeDb + 6.0, None)
                # # NOTE: -6.0 dB = half volume !
                speak("System volume has been incremented")
                print("System volume has been incremented")

            elif 'search ' and ' on amazon' in query:
                print("Searching on Amazon....")
                speak("Searching on Amazon")
                query = query.replace("search ", "")
                query = query.replace(" on amazon", "")
                query = query.replace(" ", "+")
                obj = (f"https://www.amazon.in/s?k={query}&ref=nb_sb_noss")
                webbrowser.open(f"{obj}")


            elif 'search ' and ' on google' in query:
                print("Searching on Google....")
                speak("Searching on Google")
                query = query.replace("search ", "")
                query = query.replace(" on google", "")
                query = query.replace(" ", "+")
                obj = (f"https://www.google.com/search?q={query}")
                webbrowser.open(f"{obj}")


            # elif 'search ' and ' on youtube' in query:
            #     print("Searching on YouTube....")
            #     speak("Searching on YouTube")
            #     query = query.replace("search ", "")
            #     query = query.replace(" on youtube", "")
            #     query = query.replace(" ", "+")
            #     obj = (f"https://www.youtube.com/results?search_query={query}")
            #     webbrowser.open(f"{obj}")

            elif 'play' and 'on youtube' in query:
                speak("Playing your song now...")
                print("Playing your song now...")
                query = query.replace("on youtube ", "")
                query = query.replace("play ", "")
                query = query.replace(" ", "+")
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
                vidId = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                video = (f"https://www.youtube.com/watch?v={vidId[0]}")
                webbrowser.open(f"{video}")

                                

        except Exception as e:
            print(f"The following error has occured: {e}")
        
        