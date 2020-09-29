import discord

from discord.ext import commands
import asyncio

import time

from datetime import date
import datetime

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = ''
   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="/")

#First thing that will run upon starting the script

#print('1')


def yeye():
    today = datetime.date.today()
    someday = datetime.date(2020, 9, 26)
    diff = today - someday
    nput = diff.days
    return nput
  
        

@bot.event
async def on_message(message):

    guild = bot.get_guild(759657204184907797)
    channel = bot.get_channel(760344073365225483)
    channel2 = bot.get_channel(760394856773320735)
    channel3 = bot.get_channel(760345000906719252)

    member_count = len(message.guild.members)


    strmem = str(member_count)

    print(message.content)
    x = str(message.content)

    nowtime = date.today()
    wy = (nowtime)
       
    y = str(wy)



 

    z = ("Total Members :" + strmem)

    print(member_count)
    xi = str(yeye())

    xii = ("Server Age: " + xi + " Days Old")

    print("____________")
    print(z)
    print(y)
    print(xii)

    await channel.edit(name=z)
    await channel2.edit(name=y)
    await channel3.edit(name=xii)

    





      


#Runs the Bot       
bot.run(TOKEN)