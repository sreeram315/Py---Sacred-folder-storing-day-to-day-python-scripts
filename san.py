

nums = input().split()
nums = [int(t) for t in nums]
# nums = [2,4,2]
# print(nums[0] * (nums[1]-1) * (nums[2]-2))
ans = []
chosen = []
for c1 in range(1, nums[0]+1):
	chosen.append(c1)
	# print("------", chosen)
	for c2 in range(1, nums[1]+1):
		if c2 in chosen:
			continue
		chosen.append(c2)
		# print("*****", chosen)
		for c3 in range(1, nums[2]+1):
			if c3 in chosen:
				continue
			chosen.append(c3)
			# print("&&&&", chosen)
			if len(chosen)==3: ans.append(chosen)
			chosen = chosen[:2]
		chosen = chosen[:1]
	chosen = []

print(len(ans))
for arr in ans:
	[print(t, end = ' ') for t in arr]
	print('')


