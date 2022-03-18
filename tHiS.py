import random
import sys
# sys.stdout = open('x.txt', 'w+')
string = 'this is once in a lifetime opportunity wira you have to grab it with both hands'
flag = False

for i in range(len(string)):
	if flag:
		print(string[i].upper(), end = '')
	else:
		print(string[i].lower(), end = '')
	if flag:
		flag = False
	else:
		flag = True



'''
import random
import sys
# sys.stdout = open('x.txt', 'w+')
string = 'this is once in a lifetime opportunity wira you have to grab it with both hands'

for i in range(len(string)):
	if random.randint(0,1):
		print(string[i].upper(), end = '')
		continue
	print(string[i].lower(), end = '')
'''
