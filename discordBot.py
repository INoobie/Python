import discord, time, random
from discord.ext import commands
from discord import *

def authorprint(c, d):
    if c == 'ctx':
        print(f'Author: {c.author} Command: {d}')
    else:
        print('I cannot find that command used!')

token = '' # bot token

prefix = '!' # bot prefix

presence = 'Noobie#4334' # bots presence

intents = discord.Intents.all()

Client = commands.Bot(command_prefix=prefix, intents=intents)

@Client.event
async def on_ready():
    print('bot online!')
    await Client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=presence))

@Client.command()
async def hello(ctx):
    authorprint(ctx, 'hello')
    await ctx.author.reply('Hello!')

Client.run(token)
