import discord
import asyncio
from discord.ext import commands
import time
from cogs.utils import checks


class main():


	def __init__(self, bot):
		self.bot = bot
		version = self.bot.version


	conn = sqlite3.connect('{}'.format(self.bot.db))
	c = conn.cursor()


	@commands.command(name='1337', hidden=True, pass_context=True)
	@checks.is_main_server()
	async def _charge(self, ctx):
		"""Congrats! you found an easter egg!"""
		server = ctx.message.server
		author = ctx.message.author
		server = ctx.message.server
		await self.bot.say('Logging in...')
		time.sleep(4)
		await self.bot.say('Welcome agent {}'.format(author.name))
		await self.bot.say('Grabbing tasks...')
		for row in c.execute('SELECT tasks FROM servers WHERE sid = ("%s")' % server.id):
			print(row)
			
		time.sleep(4)
