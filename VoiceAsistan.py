import playsound
import  speech_recognition as sr
from gtts import gTTS
import random
import time



def konuş(yazı):
    tts = gTTS(text = yazı, lang= "tr")
    dosya_ismi = "ses"+ str(random.randint(0,1000000000000000000000)) + ".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)

def sesi_kaydet():
    r = sr.Recognizer()

    with sr.Microphone() as kaynak:
        ses = r.listen(kaynak)

        söylenen_cümle = ""

        try:
            söylenen_cümle = r.recognize_google(ses, language="Tr-tr")
            print(söylenen_cümle)

        except Exception:
            konuş("afbuyur?")

    return söylenen_cümle


while True:

    yazı = sesi_kaydet()



    if "nasılsın" in yazı:
        konuş("iyiyim sen nasılsın")

    elif "Benim adım ne" in yazı:
        konuş("Adınız Buğra, efendim.")