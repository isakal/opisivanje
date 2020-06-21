from time import sleep
import random
import pyttsx3


engine = pyttsx3.init()

# get all the available voices on the machine
voices = engine.getProperty('voices')

# pump up the volume
engine.setProperty('volume', 10)
# slow the speaker down
engine.setProperty('rate', 160)
# set croatian language, depends on machine
engine.setProperty("voice", voices[30].id)


if __name__ == "__main__":
    while True:
        engine.say("opisivanje")
        engine.runAndWait()
        sleep(random.randint(10, 20))
