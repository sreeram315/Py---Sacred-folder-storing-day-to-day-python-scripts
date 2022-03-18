

# candidate keys



arr = ['A', 'B', 'C', 'D', 'E']
ans = []

for a1 in arr:
	# print('1')
	ans.append(a1)
	for a2 in arr:
		# print('2')
		ans.append(a1 + a2)
		for a3 in arr:
			# print('3')
			ans.append(a1 + a2 + a3)
			for a4 in arr:
				# print('4')
				ans.append(a1 + a2 + a3 + a4)
				for a5 in arr:
					ans.append(a1 + a2 + a3 + a4 + a5)
# print(ans)

for i in range(len(ans)):
	ans[i] = "".join(set(ans[i]))
	ans[i] = ''.join(sorted(ans[i]))
count = 0
final = []
for t in ans:
	if (('A' in t) or ('B' in t) or ('C' in t)) and (('D' in t) or 'E' in t):
		if t not in final:
			final.append(t)
			count += 1
print(len(final))



