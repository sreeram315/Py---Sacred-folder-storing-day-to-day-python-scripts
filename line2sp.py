# proprietary to BEERA // DO NOT COPY
handle = open('data.txt')
a = handle.readlines()

for i in range(len(a)):
	a[i] = a[i][:-1]

for i in a:
	print(i,end=' ')