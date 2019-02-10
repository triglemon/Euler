import os
from discord.ext import commands

bot = commands.Bot(command_prefix='~')
bot.connection = None


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


async def file_task():
    while True:
        if os.path.exists('command.txt'):
            with open('command.txt') as command:
                command_text = command.read()
                print(command_text)
            os.remove('command.txt')
            channel = bot.get_channel(544008926132305930)
            await channel.send(command_text)


bot.run('NDgxOTk4NjMwMDk0NjM1MDI4.D0DrlQ.D1qUhdjtOpFEFQv_e3IliclA0NQ')
