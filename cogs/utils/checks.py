from discord.ext import commands
import discord.utils


def is_owner_check(message):
	return message.author.id == '106423924614545408'

def is_owner():
	return commands.check(lambda ctx: is_owner_check(ctx.message))

def role_or_permissions(ctx, check, **perms):
	if check_permissions(ctx, perms):
		return True

	ch = ctx.message.channel
	author = ctx.message.author
	if ch.is_private:
		return False # can't have roles in PMs

	role = discord.utils.find(check, author.roles)
	return role is not None

def mod_or_permissions(**perms):
	def predicate(ctx):
		return role_or_permissions(ctx, lambda r: r.name in ('Moderator', 'Administrator'), **perms)

	return commands.check(predicate)

def admin_or_permissions(**perms):
	def predicate(ctx):
		return role_or_permissions(ctx, lambda r: r.name == 'Administrator', **perms)

	return commands.check(predicate)

def is_in_servers(*server_ids):
	def predicate(ctx):
		server = ctx.message.server
		if server is None:
			return False
		return server.id in server_ids
	return commands.check(predicate)

def is_main_server():
	return is_in_servers('145079846832308224')

def embed_perms(message):
	try:
		check = message.author.permissions_in(message.channel).embed_links
	except:
		check = True

	return check