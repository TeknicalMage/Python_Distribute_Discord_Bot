#Made by Teknical Mage 10/23/18
import discord

from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = ''

players = {}
   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="#")

#First thing that will run upon starting the script
@bot.event 
async def on_ready():
    print ("Good to Go")
    print ("I am running on " + bot.user.name)
    print ("with the ID" + bot.user.id)
    
#Example of the bot responding to a command    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("ping")
    print ("user has pinged")

#Joins Voice Channel    
@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)

#Leave Voice Channel        
@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()
    
#Playing a youtube link
@bot.command(pass_context=True)
async def play(ctx, url): 
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

#Basically #Help, but not dumb        
@bot.command(pass_context=True)
async def commands(ctx):
    await bot.say("#help - get a list of commands \n#ping - ping the bot \n#echo - repeat a line you want \n#join - join the server \n#leave - leave the server")   

#Another text test    
@bot.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await bot.say(output)

#Runs the Bot       
bot.run(TOKEN)

