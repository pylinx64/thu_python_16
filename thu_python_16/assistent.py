import pyttsx3

tts = pyttsx3.init()
# настройка скорости 
tts.setProperty('rate', 150)

# создаем команду для говорения
def sayBot(text):
    tts.say(text)
    print(text)
    tts.runAndWait()

text=input()
sayBot(text)
