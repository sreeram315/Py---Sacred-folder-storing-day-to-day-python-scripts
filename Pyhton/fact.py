a=int(input("Enter a number to find its factorial:		"))
def fact(a):
	b=a-1
	while(b!=0):
		a=a*b
		b-=1
	return a
d=fact(a)
print(d)
import time
time.sleep(22)
