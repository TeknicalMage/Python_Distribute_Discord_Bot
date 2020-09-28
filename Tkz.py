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
    #Mod report Channel
    channel = bot.get_channel(759982094708506644)
    #ReportBoi Role
    role = message.guild.get_role(759898325796651078)
    if message.content.startswith('`report') and 'everyone' not in message.content:
        print('Recieved')
        print(message.author)
        print(message.content)

        x = str(message.content)    
        z = str(message.author)

        mt = x.replace('`report', '')

        print('_____')
        print(mt)
        

        member = message.author

        time.sleep(.5)

        emoji = ("🎫") 

        await message.add_reaction(emoji)

        member = message.author


 
        await member.add_roles(role)
        await channel.send(member.mention + ' reported:' + mt)
        time.sleep(2)

        #await channel.send(member.mention)


    elif message.content.startswith('`resolved'):
        print('')
        member = message.author

        await member.remove_roles(role)

        print(member)

    elif message.content.startswith('`resolveme'):
        print('asdf')
        #print(mfk)

        #mt = mfk.replace('`resolve ', '')

        

        #print(mt)
        #member = mt
        #print(member)

        #await member.remove_roles(role)
        



    else:
        print("")









      


#Runs the Bot       
bot.run(TOKEN)