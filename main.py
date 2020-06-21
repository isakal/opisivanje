from time import sleep
import random
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('volume', 10)
# engine.setProperty('voice', voices.id[])

if __name__ == "__main__":
    while True:
        # print("opisivanje")
        engine.say("opisivanje")
        engine.runAndWait()
        sleep(random.randint(10, 20))
