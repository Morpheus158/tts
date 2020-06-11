from gtts import gTTS
import os
from playsound import playsound
import wikipedia

def say(text):
    tts = gTTS(text=text, lang="cs")
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")
    
def wiki_get_summary(keyword):
    wikipedia.set_lang("cs")
    text = wikipedia.summary(keyword)
    return text

#say(wiki_get_summary("gravitace"))
print(wiki_get_summary(""))
