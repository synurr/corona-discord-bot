import discord
from discord.ext import commands
import asyncio
import random
import datetime
import youtube_dl
import time 
import traceback
import logging
import os
import typing

from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = 'c?')

players = {}

#bot startup 
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="hand washing simulator 2020")) 


print("""

(ascii logo here if you want, if not delete)

""")

print('bot online') 

#on error
@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

#member joined
@client.event
async def on_member_join(member):
	print(f'{member} has joined')

#member removed
@client.event
async def on_member_remove(member):
	print(f'{member} has left')


#corona version
@client.command(pass_context=True)
async def coronaversion(ctx):
	await ctx.send('1')

#auto clear/purge
@client.command(pass_context=True)
@has_permissions(manage_messages=True)
async def autoclear(ctx, amount=10):
	await ctx.channel.purge(limit=amount)
	await ctx.send('cleared 10 messages')

#clear/purge
@client.command(pass_context=True)
@has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
	await ctx.channel.purge(limit=amount)
	await ctx.send('cleared messages.')

#hello
@client.command(pass_context=True)
async def hello(ctx):
	await ctx.send('Hello {0.display_name}'.format(ctx.author))

#shutdown
@client.command(pass_context=True)
@commands.has_any_role('shutdown', %role id here%)
async def shutdown(ctx):
    await ctx.send('Goodbye cruel world')
    print('Bot shut down')
    await client.close()

#ping 
@client.command(pass_context=True)
async def ping(ctx):
        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)
        await ctx.send(f"{ping} MS")

#cool
@client.command(pass_context=True)
async def cool(ctx):
    await ctx.send('Yes, the bot is cool.')

#codedin?
@client.command(pass_context=True)
async def codedin(ctx):
	await ctx.send('I am coded in discord.py')
	
#whatversionofpython
@client.command(pass_context=True)
async def versionofpython(ctx):
	await ctx.send('The bot is made in python 3')

#corona time
@client.command(pass_context=True)
async def whattimeisit(ctx):
	await ctx.send('ITS CORONA TIME https://imgur.com/a/tj9S84W')

#thoughts
@client.command(pass_context=True)
async def thoughts(ctx):
	await ctx.send(random.choice(["I love it", "I hate it", "I really love it", "I really fucking hate it and you're gay", "you're gay"]))

#why
@client.command(pass_context=True)
async def why(ctx):
	await ctx.send('just because')

#goodnight
@client.command(pass_context=True)
async def goodnight(ctx):
    await ctx.send('Goodnight {0.display_name}'.format(ctx.author))

#bedtime
@client.command(pass_context=True)
async def bedtime(ctx):
    await ctx.send('My bed time is at 8:30')

#dad
@client.command(pass_context=True)
async def dad(ctx):
    await ctx.send('My dad is %name here%')

#whoshotx
@client.command(pass_context=True)
async def whoshotxxtentacion(ctx):
    await ctx.send('heres the shooter! https://imgur.com/a/SwYvl8T')

#whoshottupac
@client.command(pass_context=True)
async def whoshottupac(ctx):
    await ctx.send('driveby! https://imgur.com/a/fcaFiOu')

#yeet
@client.command(pass_context=True)
async def yeet(ctx):
    await ctx.send('YEET https://imgur.com/a/1EZUr2L')

#justinbieber
@client.command(pass_context=True)
async def bieber(ctx):
    await ctx.send('Beaver boy https://imgur.com/a/pxd81AR')

#github(please leave this ty <3)
@client.command(pass_context=True)
async def github(ctx):
	await ctx.send('Here is the discord.py github: https://github.com/Rapptz/discord.py')
    
#invite
@client.command(pass_context=True)
async def invite(ctx):
    await ctx.send('%invite link here%')

#agree or dont
@client.command(pass_context=True)
async def agreeornot(ctx):
    await ctx.send(random.choice(["I agree", "I dont agree retard"]))

#didnt ask
@client.command(pass_context=True)
async def didntask(ctx):
    await ctx.send('Damn, I didnt ask either')

#corona
@client.command(pass_context=True)
async def corona(ctx):
    await ctx.send('Drink up! https://imgur.com/a/O2ygcFl')

#commands
@client.command(pass_context=True)
async def commands(ctx):  #not an error :)
    await ctx.send("**corona version,autoclear,clear,hello,shutdown,ping,cool,codedin,versionofpython,whattimeisit,thoughts,why,goodnight,bedtime,dad,whoshotxxxtentacion,whoshottupac,yeet,bieber,github,invite,agreeornot,didntask,corona,nice**")

#nice
@client.command(pass_context=True)
async def nice(ctx):
    await ctx.send('nice {0.display_name}'.format(ctx.author))
    await ctx.send('69 420')

#repeat
@client.command(pass_context=True)
async def repeat(ctx, *, message=None):
    message = message or "Please provide the message to be repeated"
    await ctx.message.delete()
    await ctx.send(message)

#8ball
@client.command(pass_context=True)
async def eightball(ctx):
    await ctx.send(random.choice(["It is certain :8ball:",
                                   "It is decidedly so :8ball:",
                                   "Without a doubt :8ball:",
                                   "Yes, definitely :8ball:",
                                   "You may rely on it :8ball:",
                                   "As I see it, yes :8ball:",
                                   "Most likely :8ball:",
                                   "Outlook good :8ball:",
                                   "Yes :8ball:",
                                   "Signs point to yes :8ball:",
                                   "Reply hazy try again :8ball:",
                                   "Ask again later :8ball:",
                                   "Better not tell you now :8ball:",
                                   "Cannot predict now :8ball:",
                                   "Concentrate and ask again :8ball:",
                                   "Don't count on it :8ball:",
                                   "My reply is no :8ball:",
                                   "My sources say no :8ball:",
                                   "Outlook not so good :8ball:",
                                   "Very doubtful :8ball:"]))




#bottles on the wall(this doesnt really work as intended, it should keep going the list)
@client.command(pass_context=True)
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))


#dice
@client.command(pass_context=True)
async def dice(ctx):
       await ctx.send('your roll {0.display_name}'.format(ctx.author))
       await ctx.trigger_typing()
       await ctx.send((random.choice(["one", "two", "three", "four", "five", "six",])))
       

#add
@client.command(pass_context=True)
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

#slap
@client.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    embed = discord.Embed(title="Wapow!", description="**{1}** slaps **{0}**!".format(member.name, ctx.message.author.name), color=0x176cd5)
    await ctx.send("https://imgur.com/a/RoygSd6")
    await ctx.send(embed=embed)


#ban
@client.command(passs_context=True)
@has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} has been banned")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You Don't have permission to ban people")

#mute
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a user")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute users")

#unmute
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute users")


#send announcements
@client.command(pass_context=True)
@has_permissions(manage_messages=True)
async def announcement(ctx, *, message=None):
    message = message or "Please provide a message to be announced"
    channel = client.get_channel(%your channel id%)
    await ctx.message.delete()
    await ctx.send(message)
    await ctx.send('announcement made')
    await channel.send(message)

        

client.run('%your token here%')

#where it has "% %" please fill in your own information