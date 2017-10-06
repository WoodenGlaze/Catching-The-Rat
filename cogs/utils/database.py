########################################################################
#     ALL RIGHTS RESERVED, CREATED BY TONY USING THE DISCORD.PY API    #
#  CATCHING THE RAT IS A RESERVED TRADE NAME BY TONY STARK(DION SOREL) #
#  ANY NAMES OR OTHERWISE SIMILAR THINGS ARE A COINCIDENCE AND NOT ON  #
# 								PURPOSE								   #
########################################################################
#						CODE STARTS ON LINE 10						   #
########################################################################

from discord.ext import commands
import discord.utils
import sqlite3


database = './db/database.db'



def create_task(ctx, tname, tdesc):
	tcontractor = ctx.message.author
	tserver = ctx.message.server
	tserverid = tserver.id
	tcontractorid = tcontractor.id
	id = None
	num1 = random.randrange(0, 9) * random.randrange(0, 1) * random.randrange(0, 100)
	num2 = random.randrange(0, 9) * random.randrange(0, 25) * random.randrange(0, 75)
	num3 = random.randrange(0, 9) * random.randrange(0, 50) * random.randrange(0, 50)
	num4 = random.randrange(0, 9) * random.randrange(0, 75) * random.randrange(0, 25)
	num5 = random.randrange(0, 9) * random.randrange(0, 100) * random.randrange(0, 1)
	#Multipies first randomly generated number with two other randomly generated numbers to make it harder to guess. (Note: If the first number is a zero it doesn't make it harder, just returns a 0, as 0 * anything is still zero)
	finish = '{0}{1}{2}{3}{4}'.format(num1, num2, num3, num4, num5)
	tfinish = finish
	tagent = None
	tagentid = None
	tvalue = 100
	c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, tserver, tserverid, tname, tdesc, tcontractor, tcontractorid, tfinish, tagent, tagentid, tvalue)) 
	for created in c.execute('SELECT * FROM tasks WHERE tname=("%s")' % tname):
		print(created)
	await self.bot.say(created)
	conn.commit()	