import discord
import asyncio
import sqlite3
import random
from discord.ext import commands
from cogs.utils import checks


class keygen:


	def __init__(self, bot):
		self.bot = bot
	conn = sqlite3.connect('{}'.format(self.bot.db))
	c = conn.cursor()


	@commands.command(pass_context=True, hidden=True)
	@checks.is_owner()
	async def nuke(self, ctx):
		c.execute('''DROP TABLE players''')
		c.execute('''DROP TABLE servers''')
		c.execute('''DROP TABLE tasks''')
		c.execute('''CREATE TABLE players
			(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			uid INTEGER NOT NULL,
			uname VARCHAR NOT NULL,
			advancement VARCHAR,
			score INTEGER)
			''')
		c.execute('''CREATE TABLE servers
			(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			sname VARCHAR NOT NULL,
			sid INTEGER NOT NULL)
			''')
		c.execute('''CREATE TABLE tasks
			(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			tserver VARCHAR NOT NULL,
			tserverid INTEGER NOT NULL,
			tname VARCHAR NOT NULL,
			tdesc VARCHAR NOT NULL,
			tcontractor VARCHAR NOT NULL,
			tcontractorid INTEGER NOT NULL,
			tfinish INTEGER NOT NULL
			)''')
		c.commit()
		await self.bot.say('Nuked Database and recreated it!')

	@commands.command(pass_context=True, hidden=True)
	@checks.is_owner()
	async def createdb(self, ctx)
		c.execute('''CREATE TABLE players
			(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			uid INTEGER NOT NULL,
			uname VARCHAR NOT NULL,
			advancement VARCHAR,
			score INTEGER)
			''')
		c.execute('''CREATE TABLE servers
			(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			servername VARCHAR NOT NULL,
			sid INTEGER NOT NULL)
			''')
		c.execute('''CREATE TABLE tasks
			(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			tserver VARCHAR NOT NULL,
			tserverid INTEGER NOT NULL,
			tname VARCHAR NOT NULL,
			tdesc VARCHAR NOT NULL,
			tcontractor VARCHAR NOT NULL,
			tcontractorid INTEGER NOT NULL,
			tfinish INTEGER NOT NULL,
			tagent VARCHAR NOT NULL,
			tagentid VARCHAR NOT NULL
			)''')
		c.commit()
		print('Created Database!')
		await self.bot.say('Created database!')


	@commands.command(pass_context=True, hidden=True)
	@checks.admin_or_permissions()
	async def servers(self, ctx)
		r1 = random.randrange(0,9)
		r2 = random.randrange(0,9)
		r3 = random.randrange(0,9)
		#First range of numbers made.
		r4 = random.randrange(0,9)
		r5 = random.randrange(0,9)
		r6 = random.randrange(0,9)
		#Second range of numbers made.
		r7 = random.randrange(0,9)
		r8 = random.randrange(0,9)
		r9 = random.randrange(0,9)
		#Third range of numbers made.
		r10 = random.randrange(0,9)
		r11 = random.randrange(0,9)
		r12 = random.randrange(0,9)
		#Last range made, combining it into a name.
		sname = '{0}{1}{2}.{3}{4}{5}.{6}{7}{8}.{9}{10}{11}'.format(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12)
		#Create server algorithm goes here
		#
		servercreation = await self.bot.create_server(name=sname)
		server = discord.utils.get(server, name=sname)
		get_owner = discord.utils.get(member, id=self.bot.owner)
		if servercreation == False:
			await self.bot.say('Server creation failed, contact <@{}>'.format(self.bot.owner))
		else:
			await self.bot.say('Server creation succeeded, created server with name {0.name} (ID: {0.id})'.format(server))
			invlink = await self.bot.create_invite(server)
			await self.bot.send_message(get_owner, content='{}'.format())
		sid = server.id
		c.execute("INSERT INTO servers VALUES (?, ?, ?)", (id, sname, sid))
		c.commit()


	@commands.command()
	


	@commands.command()
		