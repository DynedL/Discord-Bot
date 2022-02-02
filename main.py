import discord
from discord.ext import commands
from discord.ext.commands import bot
import os
import keep_alive
#there ya go
keep_alive.keep_alive()

bot = commands.Bot(command_prefix='!')

client = discord.Client()

@client.event
async def on_ready():
 print('We have logged in as {0.user}.format(client)')

@client.event
async def on_message(message):
 if message.author == client.user:
   return
	
 if "screening" in message.content:
		await message.channel.send(file=discord.File('ok.png'))
 if 'test' in message.content:
   await message.channel.send('<@&899066966424289301>')

@bot.command()
async def message(ctx, user:discord.Member, *, message=None):
	message = "poke"
	embed = discord.Embed(title=message)
	await user.send(embed=embed)


my_secret = os.environ['token']

client.run(os.environ['token'])
