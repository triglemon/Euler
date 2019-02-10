import os
import keyboard
import speech_recognition as sr
from discord.ext import commands

bot = commands.Bot(command_prefix='~')
bot.connection = None
recognizer = sr.Recognizer()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.loop.create_task(file_task())


@bot.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        bot.connection = await channel.connect()


@bot.command(pass_context=True)
async def leave(ctx):
    clients = {client.channel.id: client for client in bot.voice_clients}
    print(clients)
    origin = ctx.author.voice.channel.id
    print(origin)
    print(origin in clients)
    if origin in clients:
        await clients[origin].disconnect()


async def open_mic():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print("Say something!")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_sphinx(audio)
        if command in ["pies", "pods", "pas", "paws"]:
            command = "pause"
        return command
        # with open('log', 'a') as log_file:
        #     log_file.write(command + '\n')
        pass
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        pass
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        pass


async def keyboard_detect()

async def file_task():
    while True:
        if os.path.exists('command.txt'):
            with open('command.txt') as command:
                command_text = command.read()
                print(command_text)
            os.remove('command.txt')
            channel = bot.get_channel(521540280629854218)
            await channel.send(command_text)


bot.run()
