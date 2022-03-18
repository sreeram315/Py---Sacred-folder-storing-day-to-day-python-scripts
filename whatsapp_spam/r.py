



f = open("t.txt", "r")
count = 0
nw = 0
for x in f.readlines():
	for word in x.split():
		print(word)
		nw += 1
	count += 1
	if(count==124): break

print(nw)