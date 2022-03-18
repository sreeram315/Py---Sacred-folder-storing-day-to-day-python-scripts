
# s1 = 'mwupz'
# s2 = 'harry'
# print(s1, s2)
# for i in range(len(s1)):
# 	print(ord(s2[i]) - ord(s1[i]), end = ' ')
# print('')
# s1 = 'indap'
# s2 = 'draco'

# print(s1, s2)
# for i in range(len(s1)):
# 	print(ord(s2[i]) - ord(s1[i]), end = ' ')
# print('')
# s1 = 'zllrerlf'
# s2 = 'hermione'

# print(s1, s2)
# for i in range(len(s1)):
# 	print(ord(s2[i]) - ord(s1[i]), end = ' ')
# print('')


ss =  ['enokyo', 'mzcdrb', 'hyupokym', 'kuwokyo', 'mniuyo']
x = 1
flag = True
for s in ss:
	x = 1
	for i in range(len(s)-1, -1, -1):
		# print(chr(ord(s[i])-1))
		# break
		if(flag):
			print(chr(ord(s[i])-x), end = '')
		else:
			print(chr(ord(s[i])+x), end = '')
		flag = not flag
		x += 1
	print('')





