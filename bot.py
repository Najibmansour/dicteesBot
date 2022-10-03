from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import PyPDF2 as ppdf
import random 
import json
from time import sleep
from threading import Thread



if not os.path.exists('./audios/'):
    os.makedirs('./audios/')

def clear():
    os.system("clear")
#    os.system("cls")              IF ON WINDOWS UNCOMMENT THIS LINE AD COMMENT LINE ABOVE 


clear()
################# INITIALISE CONFIG #################
textInput = ''


speed = 0
lang = ''
slow = False
with open("./config.json", "r") as f:
    data = json.load(f)
    speed = data["speed"]
    lang = data["language"]
    slow = data["slow"]
    f.close()

################## VARIABLES ########################
title = ''
text = ''
titles = []
with open("./data.json", "r") as f:
    data = json.load(f)
    if data != {}:
        for i in data:
            titles.append(data[i]["title"])
        for i, title in enumerate(titles):
            print(f"{i+1}) {title}")
        
        entryNum = int(input('Which pragraph u chose?: ')) -1
        entry = data[f"{entryNum}"]
        text = entry["text"]
        title = entry["title"]
        # print(text)
   



################## LOGIC ############################

def textToSpeech(text):
    clear()
    print('Turning paragraph into audio... Might take a minute.')
    fileNum = 0
    textedit = text.split(" ")
    textSplit = [s for s in textedit if s.strip()]
    for word in textSplit:
        # print(word) 
        myobj = gTTS(text=word, lang=lang, slow=slow)
        myobj.save(f"./audios/{fileNum}.mp3")
        fileNum +=1

class SPEECH(Thread):
    def run(self):
        filesInPath = os.listdir('./audios/')
        for i in range(len(filesInPath)):
            sleep(speed)
            sound = AudioSegment.from_mp3(f"./audios/{i}.mp3")   
            play(sound)

class INPUT(Thread):
    def run(self):
        clear()
        textInput = input("> ")
        checkInput(text ,textInput)

def checkInput(text, input):
    text = text.split()
    mark = 0
    total = len(text)
    textInput = input
    textInput = textInput.split()
    for i, word in enumerate(textInput):
        
        if text[i] == word:
            mark +=1
        else:
            pass
    print(f"{mark}/{total}")
                




# textToSpeech(text)
np = INPUT()
sp = SPEECH()

sp.start()
np.start()

