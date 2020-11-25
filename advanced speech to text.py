import speech_recognition as sr
from googletrans import Translator

test=sr.Recognizer()

with sr.Microphone() as Source:
    print("SPEAK")
    audio=test.listen(Source)
    text=test.recognize_google(audio)
    print("You said: ",text)
    print()
    print("TRANSLATED VERSION")
    translator=Translator()
    translated_lang=str(input("TRANSLATE LANGUAGE: "))
    translated_sentence=translator.translate(text,src='en',dest=translated_lang.lower())
    
    with open("result.txt","a",encoding="UTF-8") as file:
        file.write(translated_sentence.text)
    print(translated_sentence.text)


