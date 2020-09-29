import discord

from discord.ext import commands
import asyncio

import time

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = ''
#Role
   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="/")

#First thing that will run upon starting the script

@bot.event
async def on_raw_reaction_add(self):
    print(self)

    member = self.member

    #print('Channel ID----------------')
    channel = bot.get_channel((760004996103667722))

    yellow = member.guild.get_role(759658281865314315)
    
    white = member.guild.get_role(760213688048287754)

    red = member.guild.get_role(760214216166342748)

    purple = member.guild.get_role(760214176139706438)

    pink = member.guild.get_role(760213751797645353)

    orange = member.guild.get_role(760214999846092820)

    green = member.guild.get_role(760215052941918240)

    cyan = member.guild.get_role(760215061666332673)

    blue = member.guild.get_role(760215061737504809)

    brown = member.guild.get_role(760215154960629830)

    black = member.guild.get_role(760215178473898074)

    channel2 = bot.get_channel(759678740723924992)
    

    #print('Emoji ID----------------')

    emojitc = (self.emoji.id)
    
    print(emojitc)

 

    if emojitc == int(760011459375136798) and channel2 == int(759678740723924992):

        print('worked')

        await member.add_roles(yellow)
        
    elif emojitc == int(760011439276163102) and channel2 == int(759678740723924992):

        print('worked')

        await member.add_roles(white)
    elif emojitc == int(760011395755802675) and channel2 == int(759678740723924992):
    
        print('worked')

        await member.add_roles(purple)
    elif emojitc == int(760011179325784084) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(blue)
    elif emojitc == int(760011345155719198) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(orange)
    elif emojitc == int(760011439276163102) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(white)
    elif emojitc == int(760011289895895070) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(green)
    elif emojitc == int(760011266755919873) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(cyan)
    elif emojitc == int(760011241711992832) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(brown)
    elif emojitc == int(760011138905145374) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(black)
    elif emojitc == int(760011368979234818) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(pink)
    elif emojitc == int(760011414676701214) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.add_roles(red)
    else: 
        print('No From me dawg')

    


@bot.event
async def on_raw_reaction_remove(self):
    print('Valid Remove')
    print(self)

    member = self.member
    print(member)

    #print('Channel ID----------------')
    channel = bot.get_channel((760004996103667722))

    yellow = member.guild.get_role(759658281865314315)
    
    #white = member.guild.get_role(760213688048287754)

    #red = member.guild.get_role(760214216166342748)

    #purple = member.guild.get_role(760214176139706438)

    #pink = member.guild.get_role(760213751797645353)

    #orange = member.guild.get_role(760214999846092820)

    #green = member.guild.get_role(760215052941918240)

    #cyan = member.guild.get_role(760215061666332673)

    #blue = member.guild.get_role(760215061737504809)

    #brown = member.guild.get_role(760215154960629830)

    #black = member.guild.get_role(760215178473898074)

    channel2 = (759678740723924992)
    

    #print('Emoji ID----------------')

    emojitc = (self.emoji.id)
    
    print(emojitc)

 

    if emojitc == int(760011459375136798) and channel2 == int(759678740723924992):

        print('worked')

        await member.remove_roles(yellow)
    elif emojitc == int(760011439276163102) and channel2 == int(759678740723924992):

        print('worked')

        await member.remove_roles(white)
    elif emojitc == int(760011395755802675) and channel2 == int(759678740723924992):
    
        print('worked')

        await member.remove_roles(purple)
    elif emojitc == int(760011179325784084) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(blue)
    elif emojitc == int(760011345155719198) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(orange)
    elif emojitc == int(760011439276163102) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(white)
    elif emojitc == int(760011289895895070) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(green)
    elif emojitc == int(760011266755919873) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(cyan)
    elif emojitc == int(760011241711992832) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(brown)
    elif emojitc == int(760011138905145374) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(black)
    elif emojitc == int(760011368979234818) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(pink)
    elif emojitc == int(760011414676701214) and channel2 == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(red)
    else: 
        print('No From me dawg')




      


#Runs the Bot       
bot.run(TOKEN)
