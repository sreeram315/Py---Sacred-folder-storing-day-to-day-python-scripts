print('\n\n')


arr = [	[1  ,2  ,3  ,4 , 5 ],
		[16 ,17 ,18 ,19, 6 ],
		[15 ,24 ,25 ,20, 7 ],
		[14 ,23 ,22 ,21, 8 ],
		[13 ,12 ,11 ,10, 9 ],
		]
done = [
		[False, False, False, False, False],
		[False, False, False, False, False],
		[False, False, False, False, False],
		[False, False, False, False, False],
		[False, False, False, False, False],
]


def print_arr(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			print(arr[i][j], end = ' ')
		print('')


def print_clock(arr):
	right = True; left = False; down = False; up = False
	ini = True
	i = 0; j=0
	count = len(arr) * len(arr);

	while(count != 0):
		if(right):
			if(not ini):
				# print(i, j)
				i += 1
				j += 1
			ini  = False
			while(j < len(arr) and done[i][j]==False):
				print(arr[i][j], end = ' ')
				done[i][j] = True
				j += 1
				count -= 1
				right = False; down = True
				# print(j, '-')
				continue

		if(down):
			j -= 1
			i+= 1
			# print(i, j)
			while(i < len(arr) and done[i][j]==False):
				print(arr[i][j], end = ' ')
				done[i][j] = True
				i += 1
				count -= 1
				down = False; left = True
				continue

		if(left):
			i -= 1
			j -= 1
			while(j < len(arr) and done[i][j]==False):
				print(arr[i][j], end = ' ')
				done[i][j] = True
				j -= 1
				count -= 1
				left = False; up = True
				continue

		if(up):
			# print(i, j)
			j += 1 
			i -= 1
			# print(i, j)
			while(i < len(arr) and done[i][j]==False):
				print(arr[i][j], end = ' ')
				done[i][j] = True
				i -= 1
				count -= 1
				up = False; right = True
				continue


print_clock(arr)

print('\n\n')