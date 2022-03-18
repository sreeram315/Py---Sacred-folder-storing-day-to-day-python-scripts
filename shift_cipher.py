


string = "PKVUADHUAAOLTAVMVYNLAYBAOPQBZADHUAAOLTAVYLTLTILYTL"

for k in range(0, 27):
	print("K = ", k, end = '  ')
	for ch in string:
		print(chr((((ord(ch)%26)+k)%26)+ord('A')), end = '')
	print('\n')
