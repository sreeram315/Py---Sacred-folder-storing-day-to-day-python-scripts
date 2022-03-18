h = open('x.txt', 'r')
for line in h.readlines():
	x = line.strip()
	if(x != ''):
		print(x)