#############################################################################################
#Working draft of how I will be executing the code, currently all code is WORKING!          #
#Consult Tony before editing THIS code, it's meant as a "Placeholder" for all FUTURE CODE!  #
#This does mean that if THIS code changes, it means most of the other code in the bot will! #
#############################################################################################
#								Code starts at line 10										#
#############################################################################################


import random
num1 = random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9)
num2 = random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9)
num3 = random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9)
num4 = random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9)
num5 = random.randrange(0, 9) * random.randrange(0, 9) * random.randrange(0, 9)
finish = '{0}{1}{2}{3}{4}'.format(num1, num2, num3, num4, num5)
print(finish.replace("0", "") * random.randrange(0, 9))
