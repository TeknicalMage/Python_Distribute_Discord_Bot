import discord

from discord.ext import commands
import asyncio

import time

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = ''
   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="/")

#First thing that will run upon starting the script


        

@bot.event
async def on_message(message):
    
    guild = bot.get_guild(759657204184907797)
    channel = bot.get_channel(760279733178466334)

    print(message)
    x = str(message.content)


  

    print(x)

    

    member_count = len(guild.members) # includes bots



    






      


#Runs the Bot       
bot.run(TOKEN)