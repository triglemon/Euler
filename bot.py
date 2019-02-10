import os
import keyboard
import speech_recognition as sr
from discord.ext import commands

with open('token') as token_file:
    token = token_file.read()
bot = commands.Bot(command_prefix='~')
bot.connection = None

channel_id = 544008926132305930

recognizer = sr.Recognizer()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.loop.create_task(keyboard_detect())


@bot.command(pass_context=True)
async def yeet(ctx):
    await ctx.send("Mageet")


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


def open_mic():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=3)
        print("Say something!")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_sphinx(audio)
        print(f"Recognized command: {command}")
        return command
        # with open('log', 'a') as log_file:
        #     log_file.write(command + '\n')
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        pass
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        pass


async def keyboard_detect():
    while True:
        keyboard.wait('up')
        command = open_mic()
        if command:
            if command in ["pies", "pods", "pas", "paws"]:
                command = "pause"
            channel = bot.get_channel(channel_id)
            await channel.send(command)

bot.run(token)
