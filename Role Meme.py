import discord

from discord.ext import commands
import asyncio

import time

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = 'NzU5ODc4NDU2NDg1NDc4NDQx.X3D59Q.p6v8YLfbj4IZlaxPMYynjXuLcog'
   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="/")

#First thing that will run upon starting the script

@bot.event
async def on_raw_reaction_add(self):
    print(self)

    member = self.member

    #print('Channel ID----------------')
    channel = bot.get_channel((760004996103667722))
    role1 = member.guild.get_role(759898325796651078)
    #channelc = 

    

    #print('Emoji ID----------------')

    emojitc = str(self.emoji)
    print(emojitc)
    channel2 = (self.channel_id)

    if emojitc == ('🎮') and channel2 == (760004996103667722):
        print('worked')
        print(emojitc)

        await member.add_roles(role1)
        await channel.send('Role Assigmnet Here')
    else: 
        print('No From me dawg')

    


    

    #bot.get_channel()
  
    #print(payload)
   

    






      


#Runs the Bot       
bot.run(TOKEN)