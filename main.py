from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot
from cogs.utils import checks
import random
import sqlite3
import discord
import asyncio
import json


try:
	import uvloop
except ImportError:
	pass
else:
	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


database = './cogs/db/database.db'
version = '0.1b'


initial_extensions = [
	'cogs.administration',
	'cogs.generation',
	'cogs.main'
]


def load_config():
	with open('config.json') as f:
		return json.load(f)


if True == True:
	credentials = load_config()
	token = credentials['token']
	oid = credentials['ownerid']


description = """Can you catch the rat?"""
bot = Bot(command_prefix=commands.when_mentioned_or('hn)'), description=description)


@bot.event
async def on_ready():
	print('Logged in as: {0.name} (ID:{0.id})'.format(bot.user))
	print(version)
	print('------')
	print('Bot completely initialized, ready to accept commands!')
	bot.version = version
	bot.uptime = datetime.now()
	bot.db = database
	await bot.change_presence(status=discord.Status.dnd)


@bot.event
async def on_resumed():
	print('Connection resumed.')

@bot.event
async def on_member_join(member):
	if member.id == '106423924614545408':
		server = member.server
		embed = discord.Embed(color=0x738bd7, title='Defalt has entered the server', description='`~~(8=>` CAN YOU CATCH THE RAT? `<=8)~~`')
		embed.add_field(name='Time:', value=datetime.now())
	else:
		server = member.server
		if server.id == '':
			conn = sqlite3.connect('{}'.format(bot.database))
			c = conn.cursor()
			id = None
			uid = member.id
			uname = member.name
			advancement = {}
			score = 0
			for row in c.execute('SELECT uid FROM players WHERE uid = ("%s")' % member.id):
				print(row)
				print('User already registered, ignoring...')
			else:
				c.execute("INSERT INTO players VALUES (?, ?, ?, ?, ?)", (id, uid, uname, advancement, score))
				emjoin = discord.Embed(color=0x738bd7, title='Welcome to the game', description='Welcome {} to the game!'.format(member.name))
				await bot.send_message(server, embed=emjoin)
		else:
			embed = discord.Embed(color=0x738bd7, title='Advancement made:', description='{0.name} made it to stage {1.name}'.format(member, server))
			embed.add_field(name='level:', value=server.name)
			embed.add_field(name='User:', value=member.name)
			embed.add_field(name='Time:', value=datetime.now())
	await bot.send_message(server, embed=embed)	


@bot.command(pass_context=True)
@checks.is_owner()
async def kill(ctx, member):
	await bot.kick(member)
	await bot.say('Killed member: {}'.format(member.name))

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))


bot.run(token)