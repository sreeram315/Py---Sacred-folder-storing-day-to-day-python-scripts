

string = 'PKVUADHUAAOLTAVMVYNLAYBAOPQBZADHUAAOLTAVYLTLTILYTL'
dic = {}
for ch in string:
	try:
		dic[ch] += 1
	except:
		dic[ch] = 1

print(dic)