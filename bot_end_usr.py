import discord

from discord.ext import commands
import asyncio

import time

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = 
   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="`")

#First thing that will run upon starting the script



@bot.event
async def on_voice_state_update(member, before, after):
    original = before.channel
    endstate = after.channel
    print(original) 
    print('_______________________')
    #print(endstate)

    endstatestr = str(endstate)

    originalstr = str(original)
    
    Lobby = bot.get_channel(759658109433544725)

    Lobby2 = bot.get_channel(759658603442339871)

    Lobby3 = bot.get_channel(759658627090087967)

    Lobby4 = bot.get_channel(759658645180645386)

    Lobby5 = bot.get_channel(759658667154604123)

    channel = bot.get_channel(759659065382666262)
    
    general = bot.get_channel(759657204184907801)

    print(originalstr)

    #mem2 = str(member)

    
    Channelmax = 10
    htpi = 0
    htpj = 0
    htpk = 0
    htpl = 0
    htpm = 0
    time.sleep(1)
###############################################
    if endstatestr == ('QueRoom'):
        print('Initate Move')   
        Lob1 = []
        for (i) in Lobby.members:
            Lob1.append(i)
    
            Currenti = (len(Lob1))
            htpi = int(Currenti)

        Lob2 = []
        for (j) in Lobby2.members:
            Lob2.append(j)
    
            Currentj = (len(Lob2))
            htpj = int(Currentj)

        Lob3 = []
        for (k) in Lobby3.members:
            Lob2.append(k)
    
            Currentk = (len(Lob3))
            htpk = int(Currentk)

        Lob4 = []
        for (l) in Lobby4.members:
            Lob4.append(l)
    
            Currentl = (len(Lob4))
            htpl = int(Currentl)
        
        Lob5 = []
        for (m) in Lobby5.members:
            Lob4.append(m)
    
            Currentm = (len(Lob5))
            htpm = int(Currentm)
###############################################

        if htpi < Channelmax:
            await member.move_to(Lobby)
            #print(htp) 
        else:
            if htpj < Channelmax:
                await member.move_to(Lobby2)
            elif htpk < Channelmax:
                await member.move_to(Lobby3)
            elif htpl < Channelmax:
                await member.move_to(Lobby4)
            elif htpm < Channelmax:
                await member.move_to(Lobby5)
            else:
                print("Room Full")
                await channel.send('Room Full. Try again Later')

                await member.move_to(general)   

        

   
###########################################
@bot.command()
async def showe(ctx):
    member_list = ' '
    for member in ctx.message.guild.members:
        member_list += member.name + ' '
        
    print(member_list)
###########################################

@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)
   
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


###########################################
@bot.command()
async def grab(ctx):
    #member = ctx.message.guild.get_member(362748893022126091)
    #channel = ctx.member.voice.channel
    print(ctx.guild.voice_channels)

    #print(ctx.guild.voice_channels)
###########################################

    
@bot.command()
async def general(ctx, member: discord.Member):
    #print(ctx.author.voice.channel.id)
    x = bot.get_channel(481263163753496590)
    
    await member.move_to(x)

@bot.command()
async def Gen1(ctx, member: discord.Member):
    #print(ctx.author.voice.channel.id)
    x = bot.get_channel(758379379365118054)
    
    await member.move_to(x)


@bot.command()
async def channel_check(ctx):
    vc = ctx.guild.get_channel(759657204184907801)
    yuh = []

    for (i) in vc.members:
        yuh.append(i)
    
    #print(yuh)
    Current = (len(yuh))
    await ctx.send(Current)

        


#Runs the Bot       
bot.run(TOKEN)

