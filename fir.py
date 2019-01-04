# proprietary to BEERA // DO NOT COPY


import re

handle = open("regexx.txt")

lines = handle.readlines()
sum=0
for line in lines:
	print(line)
	lit = re.findall('[0-9]+',line)
	for i in lit: sum+=int(i)

print(sum)