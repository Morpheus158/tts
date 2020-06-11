import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile("coje.wav") as source:
    audio_text = r.listen(source)

    try:

        text = r.recognize_google(audio_text)
        print("Working...")
        print(text)
    
    except:

        print("Run again")