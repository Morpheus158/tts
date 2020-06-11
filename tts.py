# coding: utf8

import pyttsx3
#from tkinter import Tk, StringVar, Entry, Button
import codecs

language = 2

engine = pyttsx3.init()

filee = open("qwe.txt","r", encoding="Windows-1250")
#filee = codecs.open("qwe.txt", "r", "ISO-8859-16")

text = filee.read()

voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_csCZ_Jakub"
voice = engine.getProperty('voices')[language]
engine.setProperty('voice', voice.id)

engine.say(text)
print(text)
engine.runAndWait()

"""def say_something():
    engine.say(text_value.get())
    engine.runAndWait()

window = Tk()

text_value = StringVar()
text_entry = Entry(window, textvariable=text_value, width=30)
text_entry.grid(row=1, column=1)

say_button = Button(window, text="Mluv", command=say_something)
say_button.grid(row=3, column=0, columnspan=2)

window.mainloop()"""
