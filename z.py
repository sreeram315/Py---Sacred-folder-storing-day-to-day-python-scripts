S = [ 1, 2, 3, 4, 5, 6, 7]
m = 4
count = 0

print("")
for x in S:
	if x < m:
		count += 1
		print(x, end = ' ')
print(f"\nCount = {count}\n")
count = 0
for x in S:
	if x == m:
		count += 1
		print(x, end = ' ')
print(f"\nCount = {count}")
print("")
count = 0
for x in S:
	if x > m:
		count += 1
		print(x, end = ' ')
print(f"\nCount = {count}\n")


