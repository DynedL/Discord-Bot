import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command
async def hello(ctx):
	await ctx
