import speech_recognition as sr
import keyboard
from discord.ext import commands

bot = commands.Bot(command_prefix='~')

recognizer = sr.Recognizer()


def open_mic():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print("Say something!")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_sphinx(audio)
        if command in ["pies", "pods", "pas", "paws"]:
            command = "pause"
        with open('command.txt', 'w') as command_file:
            command_file.write(command)
            command_file.close()
        # with open('log', 'a') as log_file:
        #     log_file.write(command + '\n')
        pass
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        pass
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        pass


while True:
    keyboard.wait('=')
    open_mic()
