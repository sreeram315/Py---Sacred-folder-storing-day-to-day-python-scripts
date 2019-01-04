# proprietary to BEERA // DO NOT COPY


#a = 'aa'


#print(isinstance(int(a),int))
#print(isinstance(int(a),str))


#for i in range(10000000, 99999999):
#	k = str(i)
#	a = k[0:2]
#	b = k[2:4]
#	c = k[4:6]
#	d = k[6:8]

#	print(a,b,c,d)
zeros = 0
possies = 0


for i in range(1111,9999):
	if '0' in str(i):
		zeros += 1
		continue
	else:
		possies += 1

print('Zeroes = ',zeros)
print('possies = ',possies)