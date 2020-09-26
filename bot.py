import discord

from discord.ext import commands
import asyncio

#Your Discord Bots Token goes here. You can individually put it in every time you need it, but this alos works
TOKEN = ''

   
#Your going to start all of your commands with this
bot = commands.Bot(command_prefix="`")

#First thing that will run upon starting the script



@bot.event
async def on_voice_state_update(member, before, after):
    x = before
    y = after
    print(x)
    print('_______________________---')
    print(y)
    print("Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

#@bot.event
#async def on_voice_state_update(member, before, after):
    #if before.channel is None and after.channel is not None:
        #if after.channel.id == [481263163753496590]:
            #await member.guild.system_channel.send("Alarm!")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
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
    vc = ctx.guild.get_channel(481263163753496590)
    yuh = []

    for (i) in vc.members:
        yuh.append(i)
    
    print(yuh)
    Current = (len(yuh))

    ChannelMax=2

    if Current > ChannelMax:    
        await ctx.send("A SACRIFICE MUST BE MADE")
    else:
        await ctx.send("Actually go fuck yourself")
        



    #while x > 50000:
        #print('false')
        
    #print(vc.members)
 

#Runs the Bot       
bot.run(TOKEN)

