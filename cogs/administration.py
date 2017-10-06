import discord
import asyncio
from cogs.utils import checks

class Administration():
	def __init__(self, bot):
		self.bot = bot
		version = self.bot.version


	@commands.command(hidden=True)
	@checks.is_owner()
	async def load(self, *, module : str):
		"""Loads a module"""
		try:
			self.bot.load_extension('cogs.'+module)
		except Exception as e:
			await self.bot.say('\N{PISTOL}')
			await self.bot.say('{}: {}'.format(type(e).__name__, e))
		else:
			await self.bot.say('\N{OK HAND SIGN}')


	@commands.command(Hidden=True)
	@checks.is_owner()
	async def unload(self, *, module : str):
		"""Unloads a module"""
		try:
			print('Unloading {}'.format(module))
			self.bot.unload_extension('cogs.'+module)
		except Exception as e:
			await self.bot.say('\N{PISTOL}')
			await self.bot.say('{}: {}'.format(type(e).__name__, e))
		else:
			await self.bot.say('\N{OK HAND SIGN}')


	@commands.command(name='reload', hidden=True)
	@checks.is_owner()
	async def _reload(self, *, module : str):
		"""Reloads a module"""
		try:
			self.bot.unload_extension('cogs.'+module)
			self.bot.load_extension('cogs.'+module)
		except Exception as e:
			await self.bot.say('\N{PISTOL}')
			await self.bot.say('{}: {}'.format(type(e).__name__, e))
		else:
			await self.bot.say('\N{OK HAND SIGN}')


	@commands.command(pass_context=True)
	@checks.mod_or_permissions()
	async def kick(member : discord.Member):
		server = ctx.message.server
		await self.bot.kick(member)
		await self.bot.say('Kicked {0.name} from {1.name}'.format(member, server))


	@commands.command(pass_context=True)
	@checks.admin_or_permissions()
	async def ban(ctx, member : discord.Member):
		author = ctx.message.author
		server = ctx.message.server
		await self.bot.ban(member)
		await self.bot.say('Banned {0.name} from {1.name}'.format(member, server))
		print('{0.name} ({0.id}) banned {1.name} from {2.name}'.format(author, member, server))


#	@commands.command(pass_context=True)
#	@checks.admin_or_permissions()
#	async def setroles(ctx, member : discord.Member, role=None, role2=None, role3=None, role4=None):
#		rolefin = discord.utils.get(server.roles, name=role)
#		if role == None:
#			await self.bot.say('Specify atleast ONE role!')
#		elif role2 == None:
#			print('Role 2 not specified')
#		else:
#			rolefin2 = discord.utils.get(server.roles, name=role2)
#			final = [
#			rolefin,
#			rolefin2]
#		elif role3 == None:
#			print('Role 3 not specified')
#		else:
#			rolefin2 = discord.utils.get(server.roles, name=role2)
#			rolefin3 = discord.utils.get(server.roles, name=role3)
#			final = [
#			rolefin,
#			rolefin2,
#			rolefin3]
#		elif role4 == None:
#			print('Role 4 not specified')
#		else:
#			rolefin2 = discord.utils.get(server.roles, name=role2)
#			rolefin3 = discord.utils.get(server.roles, name=role3)
#			rolefin4 = discord.utils.get(server.roles, name=role4)
#			final = [
#			rolefin,
#			rolefin2,
#			rolefin3,
#			rolefin4]	
#
#
#		author = ctx.message.author
#		server = ctx.message.server
#		await self.bot.add_roles(mem, final)
#		print('{0.name} assigned {1} to {2.name}'.format(author, final, member))