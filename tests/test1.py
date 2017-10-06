#############################################################################################
#Working draft of how I will be executing the code, currently all code is WORKING!          #
#Consult Tony before editing THIS code, it's meant as a "Placeholder" for all FUTURE CODE!  #
#This does mean that if THIS code changes, it means most of the other code in the bot will! #
#############################################################################################
#								Code starts at line 10										#
#############################################################################################


import sqlite3
import subprocess
import random
botdb = './database.db'
conn = sqlite3.connect('{}'.format(botdb))
c = conn.cursor()

def nuke():
	c.execute('''DROP TABLE players''')
	c.execute('''DROP TABLE servers''')
	c.execute('''DROP TABLE tasks''')
	c.execute('''CREATE TABLE players
		(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		uid INTEGER NOT NULL,
		uname VARCHAR NOT NULL,
		advancement INTEGER DEFAULT 0,
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
		tfinish INTEGER NOT NULL,
		tagent VARCHAR,
		tagentid INTEGER,
		tvalue INTEGER NOT NULL
		)''')
	print('Nuked database!')

def create():
	c.execute('''CREATE TABLE players
		(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		uid INTEGER NOT NULL,
		uname VARCHAR NOT NULL,
		advancement INTEGER DEFAULT 0,
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
		tfinish INTEGER NOT NULL,
		tagent VARCHAR,
		tagentid INTEGER,
		tvalue INTEGER NOT NULL
		)''')


def register():
	id = None
	uid = 145079846832308224
	uname = 'Tony Stark'
	advancement = None
	score = 100
	c.execute("INSERT INTO players VALUES (?, ?, ?, ?, ?)", (id, uid, uname, advancement, score))
	conn.commit()


def task():
	id = None
	num1 = random.randrange(0, 9) * random.randrange(0, 1) * random.randrange(0, 100)
	num2 = random.randrange(0, 9) * random.randrange(0, 25) * random.randrange(0, 75)
	num3 = random.randrange(0, 9) * random.randrange(0, 50) * random.randrange(0, 50)
	num4 = random.randrange(0, 9) * random.randrange(0, 75) * random.randrange(0, 25)
	num5 = random.randrange(0, 9) * random.randrange(0, 100) * random.randrange(0, 1)
	#Multipies first randomly generated number with two other randomly generated numbers to make it harder to guess. (Note: If the first number is a zero it doesn't make it harder, just returns a 0, as 0 * anything is still zero)
	finish = '{0}{1}{2}{3}{4}'.format(num1, num2, num3, num4, num5)
	tserver = "Hai there!"
	tserverid = 145079846832308224
	tname = "Test Contract"
	tdesc = "This is Tony just testing the task creation thing!"
	tcontractor = "Tony Stark"
	tcontractorid = 145079846832308224
	tfinish = finish
	tagent = None
	tagentid = None
	tvalue = 100
	c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, tserver, tserverid, tname, tdesc, tcontractor, tcontractorid, tfinish, tagent, tagentid, tvalue)) 
	conn.commit()
#    c.execute("INSERT INTO stats VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, user, uid, warframe, level, mod1, mod2, mod3, mod4, mod5, mod6, mod7, mod8, mod9, mod10, mod1l, mod2l, mod3l, mod4l, mod5l, mod6l, mod7l, mod8l, mod9l, mod10l))


def view():
	for row in c.execute('SELECT * FROM tasks ORDER BY tname'):
		new = str(row).replace("(","").replace(",","").replace("'","").replace(")","")
		print(new)
	for row in c.execute('SELECT * FROM players ORDER BY uname'):
		new2 = str(row).replace("(","").replace(",","").replace("'","").replace(")","")
		print(new2)
	else:
		print('An error has occurred, code invalid')


def test_accept():
	name = "Test Contract"
	tagent = "Tony Stark"
	tagentid = 145079846832308224
	print('-------')
	for row1 in c.execute('SELECT tname FROM tasks WHERE tname = ("%s")' % name):
		pass
	for row2 in c.execute('SELECT tdesc FROM tasks WHERE tname = ("%s")' % name):
		pass
	for row3 in c.execute('SELECT tcontractor FROM tasks WHERE tname = ("%s")' % name):
		pass
	for row4 in c.execute('SELECT tserver FROM tasks WHERE tname = ("%s")' % name):
		pass
	for row5 in c.execute('SELECT tvalue FROM tasks WHERE tname = ("%s")' % name):
		print(row5)
	print(str(row5).replace("(","").replace(",","").replace("'","").replace(")",""))
	nconv = str(row5).replace("(","").replace(",","").replace("'","").replace(")","")
	conv = int(nconv)
	print(conv)
	tserver = None
	tserverid = None
	tname = None
	tdesc = None
	tcontractor = None
	tcontractorid = None
	tfinish = None
	for padv in c.execute('SELECT advancement FROM players WHERE uname =("%s")' % tagent):
		 print(padv)
		 padvanc = str(padv).replace("(","").replace(",","").replace("'","").replace(")","")
	c.execute("""
		UPDATE tasks
		SET tagent=?, tagentid=? 
		WHERE tname=?""", (tagent, tagentid, name))
	for score in c.execute('SELECT score FROM players WHERE uname=("%s")' % tagent):
		scorecor = str(score).replace("(","").replace(",","").replace("'","").replace(")","")
		print(scorecor)
		scoreconv = int(scorecor)
	if scoreconv < conv:
		c.execute("""
			UPDATE players
			SET score= score - ?
			WHERE uname=?""", (scorecor, tagent))
	else:
		c.execute("""
			UPDATE players
			SET score= score - ?
			WHERE uname=?""", (conv, tagent))
	if padvanc == 'None':
		c.execute("""
			UPDATE players
			SET advancement=?
			WHERE uname=?""", (name, tagent))
	else:
		c.execute("""
			UPDATE players
			SET advancement= advancement + ?
			WHERE uname=?""", (name, tagent))
	conn.commit()
	#taskaccepted = c.execute('INSERT INTO tasks VALUES (?, ?)', (tagent, tagentid))


def vartest(mem, score):
	print(mem)
	print(score)


def task2(tserver, tname, tdesc, tcontractor):
	id = None
	num1 = random.randrange(0, 9) * random.randrange(0, 1) * random.randrange(0, 100)
	num2 = random.randrange(0, 9) * random.randrange(0, 25) * random.randrange(0, 75)
	num3 = random.randrange(0, 9) * random.randrange(0, 50) * random.randrange(0, 50)
	num4 = random.randrange(0, 9) * random.randrange(0, 75) * random.randrange(0, 25)
	num5 = random.randrange(0, 9) * random.randrange(0, 100) * random.randrange(0, 1)
	#Multipies first randomly generated number with two other randomly generated numbers to make it harder to guess. (Note: If the first number is a zero it doesn't make it harder, just returns a 0, as 0 * anything is still zero)
	finish = '{0}{1}{2}{3}{4}'.format(num1, num2, num3, num4, num5)
#	tserver = "Hai there!"
	tserverid = 145079846832308224
#	tname = "Test Contract"
#	tdesc = "This is Tony just testing the task creation thing!"
#	tcontractor = "Tony Stark"
	tcontractorid = 145079846832308224
	tfinish = finish
	tagent = None
	tagentid = None
	tvalue = 100
	c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, tserver, tserverid, tname, tdesc, tcontractor, tcontractorid, tfinish, tagent, tagentid, tvalue)) 
	conn.commit()


#nuke()
#create()
#task()
#register()
#view()
#test_accept()


#############################################################################################
#Working draft of how I will be executing the code, currently all code is WORKING!          #
#Consult Tony before editing THIS code, it's meant as a "Placeholder" for all FUTURE CODE!  #
#This does mean that if THIS code changes, it means most of the other code in the bot will! #
#############################################################################################