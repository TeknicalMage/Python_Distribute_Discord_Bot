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

    helpaccess = member.guild.get_role(760242026242375716)

    channel2 = (759678740723924992)
  

    emojitc = (self.emoji.id)
    emojistr = (self.emoji.name)
 
    #print(emojitc)

    if emojitc == int(760011459375136798) and self.channel_id == int(759678740723924992):
        #Yellow
        print('worked')

        await member.add_roles(yellow)
        ############################################################
        await member.remove_roles(white, red, purple, orange, green, cyan, brown, black, blue, pink)
    elif emojitc == int(760011439276163102) and self.channel_id == int(759678740723924992):
        #White
        print('worked')

        await member.add_roles(white)
        ############################################################
        await member.remove_roles(yellow, red, purple, orange, green, cyan, brown, black, blue, pink)
    elif emojitc == int(760011395755802675) and self.channel_id == int(759678740723924992):
        #Purple
        print('worked')

        await member.add_roles(purple)
        ############################################################
        await member.remove_roles(yellow, white, red, orange, green, cyan, brown, black, blue, pink)
    elif emojitc == int(760011179325784084) and self.channel_id == int(759678740723924992):
        #Blue   
        print('worked')

        await member.add_roles(blue)
        ############################################################
        await member.remove_roles(yellow, white, red, purple, orange, green, cyan, brown, black, pink)
    elif emojitc == int(760011345155719198) and self.channel_id == int(759678740723924992):
        #Orange
        print('worked')

        await member.add_roles(orange)
        ############################################################
        await member.remove_roles(yellow, white, red, purple, green, cyan, brown, black, blue, pink)
    elif emojitc == int(760011439276163102) and self.channel_id == int(759678740723924992):
        #White
        print('worked')

        await member.add_roles(white)
        ############################################################
        await member.remove_roles(yellow, red, purple, orange, green, cyan, brown, black, blue, pink)
    elif emojitc == int(760011289895895070) and self.channel_id == int(759678740723924992):
        #Green
        print('worked')

        await member.add_roles(green)
        ############################################################
        await member.remove_roles(yellow, white, red, purple, orange, cyan, brown, black, blue, pink)
    elif emojitc == int(760011266755919873) and self.channel_id == int(759678740723924992):
        #Cyan   
        print('worked')

        await member.add_roles(cyan)
        ############################################################
        await member.remove_roles(yellow, white, red, purple, orange, green, brown, black, blue, pink)
    elif emojitc == int(760011241711992832) and self.channel_id == int(759678740723924992):
        #Brown
        print('worked')

        await member.add_roles(brown)
        ############################################################
        await member.remove_roles(yellow, white, red, purple, orange, green, cyan, black, blue, pink)
    elif emojitc == int(760011138905145374) and self.channel_id == int(759678740723924992):
        #Black  
        print('worked')

        await member.add_roles(black)
        ############################################################
        await member.remove_roles(yellow, white, red, purple, orange, green, cyan, brown, blue, pink)
    elif emojitc == int(760011368979234818) and self.channel_id == int(759678740723924992):
        #Pink    
        print('worked')

        await member.add_roles(pink)
        ############################################################
        await member.remove_roles(yellow, white, red, purple, orange, green, cyan, brown, black, blue)
    elif emojitc == int(760011414676701214) and self.channel_id == int(759678740723924992):
        #Red
        print('worked')

        await member.add_roles(red)
        ############################################################
        await member.remove_roles(yellow, white, purple, orange, green, cyan, brown, black, blue, pink)
    elif emojistr == ('🎫') and self.channel_id == int(759683033254723595): 
        
        print('worked')
        channel = bot.get_channel(760008213511798797)
        await member.add_roles(helpaccess)      
        #await channel.send(member.mention)
            
    else: 
        print('No From me dawg')

##########################################

@bot.event
async def on_raw_reaction_remove(self):
    print(self)

    guild = bot.get_guild(self.guild_id)
    member = guild.get_member(self.user_id)

    print(guild)
    print(member)
    

    #yellow = member.guild.get_role(759658281865314315)     

    yellow = guild.get_role(759658281865314315)
    
    white = guild.get_role(760213688048287754)

    red = guild.get_role(760214216166342748)

    purple = guild.get_role(760214176139706438)

    pink = guild.get_role(760213751797645353)

    orange = guild.get_role(760214999846092820)

    green = guild.get_role(760215052941918240)

    cyan = guild.get_role(760215061666332673)

    blue = guild.get_role(760215061737504809)

    brown = guild.get_role(760215154960629830)

    black = guild.get_role(760215178473898074)

    helpaccess = guild.get_role(760242026242375716)

   

    emojitc = (self.emoji.id)
    
    print(emojitc)
    emojistr = (self.emoji.name)

    if emojitc == int(760011459375136798) and self.channel_id == int(759678740723924992):

        print('worked')

        await member.remove_roles(yellow)
    elif emojitc == int(760011439276163102) and self.channel_id == int(759678740723924992):

        print('worked')

        await member.remove_roles(white)
    elif emojitc == int(760011395755802675) and self.channel_id == int(759678740723924992):
    
        print('worked')

        await member.remove_roles(purple)
    elif emojitc == int(760011179325784084) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(blue)
    elif emojitc == int(760011345155719198) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(orange)
    elif emojitc == int(760011439276163102) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(white)
    elif emojitc == int(760011289895895070) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(green)
    elif emojitc == int(760011266755919873) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(cyan)
    elif emojitc == int(760011241711992832) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(brown)
    elif emojitc == int(760011138905145374) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(black)
    elif emojitc == int(760011368979234818) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(pink)
    elif emojitc == int(760011414676701214) and self.channel_id == int(759678740723924992):
        
        print('worked')

        await member.remove_roles(red)
    elif emojistr == ('🎫') and self.channel_id == int(759683033254723595):
        
        print('worked')
        await member.remove_roles(helpaccess)      
    else: 
        print('No From me dawg')


    




      


#Runs the Bot       
bot.run(TOKEN)