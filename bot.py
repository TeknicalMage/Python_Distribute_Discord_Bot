import discord

from discord.ext import commands
import asyncio

import time

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = ''
   
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
    x = bot.get_channel(481268259203842049)
    channel = bot.get_channel(758371983947333733)
    nogo_channel = bot.get_channel(481268259203842049)
    general = bot.get_channel(481263163753496590)

    print(originalstr)

    mem2 = str(member)

    
    Channelmax = 2
    htp = 0
    time.sleep(1)

    if endstatestr == ('QueRoom'):
        print('Initate Move')   
        yuh = []
        for (i) in x.members:
            yuh.append(i)
    
            Current = (len(yuh))
            htp = int(Current)

        if htp < Channelmax:
            await member.move_to(x)
            #print(htp) 
        else:
            print("Room Full")
            await channel.send('Room Full. Try again Later')
            await member.move_to(general)

    elif originalstr == ('Lobby'):
        print('left')
        #print(mk3)

        
            







   
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
async def team(ctx):
    vc = ctx.guild.get_channel(481268259203842049)
    yuh = []

    for (i) in vc.members:
        yuh.append(i)
    
    #print(yuh)
    Current = (len(yuh))
    await ctx.send(Current)

    ChannelMax=2

      


#Runs the Bot       
bot.run(TOKEN)

