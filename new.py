arr = [1,3, 7,11, 19, 22, 23, 45, 67, 88]
new_el = 19
for i in range(len(arr)):
	print(arr[i], end = ' ')
	if arr[i] >= new_el:
		break
arr = arr[:i] + [new_el] + arr[i:]
print(arr)