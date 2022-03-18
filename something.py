


n = int(input())
l = 1
a = 'A'

for i in range(1, n+1):
	if i%2==1:
		for k in range(l, l+i):
			print(k, end='')
			l +=1
	if i%2==0:
		for k in range(ord(a), ord(a)+i):
			print(chr(k), end='')
			a = chr(ord(a) + 1)
	print('')



