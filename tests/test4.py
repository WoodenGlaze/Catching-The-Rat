#############################################################################################
#Working draft of how I will be executing the code, currently all code is WORKING!          #
#Consult Tony before editing THIS code, it's meant as a "Placeholder" for all FUTURE CODE!  #
#This does mean that if THIS code changes, it means most of the other code in the bot will! #
#############################################################################################
#								Code starts at line 10										#
#############################################################################################


import threading

def task1():
	print('hai!')
	print(848717882871617848712756178734617648174871635761892471723658174817785687148781635187481657818481657861857461756781516481657861785683756187356781561856371856178561875 * 378136417851874617823567812478164178647815618246817567814678364781137648164278146817462738468371468126347641)
def task2():
	print('Hello!')
def task3():
	print('How are you?')
def task4():	
	print('I\'m fine, you?')
def task5():
	print('I\'m okay!')
def task6():
	print('Yay!')

def dep1():
	t1 = threading.Thread(target=task1)
	t2 = threading.Thread(target=task2)
	t3 = threading.Thread(target=task3)

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

def dep2():
	t4 = threading.Thread(target=task4)
	t5 = threading.Thread(target=task5)


	t4.start()
	t5.start()


	t4.join()
	t5.join()

def dep3():
	d1 = threading.Thread(target=dep1)
	d2 = threading.Thread(target=dep2)

	d1.start()
	d2.start()

	d1.join()
	d2.join()

d3 = threading.Thread(target=dep3)
#d3.start()
#d3.join()
task1()
task2()
task3()
task4()
task5()


"""import random
from multiprocessing.dummy import Pool as ThreadPool

def main():

	main = [
		random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9),
		random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9),
		random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9),
		random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9)

	]

	pool = ThreadPool(80)


	results = pool.map(print, main)


	pool.close()
	pool.join()

main()"""