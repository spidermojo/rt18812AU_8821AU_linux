import discord
from discord.ext.commands import Bot

my_bot = Bot(command_prefix="Woodhouse ")

@my_bot.event
async def on_ready():
	print ("Client logged in")

@my_bot.command()
async def echo(*, message: str):
	"""Echos text following the command"""
	await my_bot.say(message)

@my_bot.command(pass_context=True)
async def hello(ctx, member: discord.Member = None):
	"""Sat hello to Woodhouse!"""
	if member is None:
		member = ctx.message.author

	await my_bot.say('Hello {0.name}. How are you today?'.format(member))

@my_bot.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
	"""Says when a member joined"""
	if member is None:
		member = ctx.message.author

	await my_bot.say('Hello, {0.name}. Can I make you some coffee?'.format(member))

@my_bot.command()
async def on_command_error(error, ctx):
	await my_bot.say('Oops. The command seemed to have broken me. Please refraing from doing it again')
