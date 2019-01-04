# proprietary to BEERA // DO NOT COPY



def printf(a):
	for i in a:
		for j in i:
			print(j,end = ' ')
		print('')
	print('')

def transpose(a):
	b = [[0 for i in range(len(a))] for _ in range(len(a[0]))]
	for i in range(len(a)):
		for j in range(len(a[i])):
			b[j][i] = a[i][j]
	return b

def product(a,b):
	ans = [[0 for i in range(len(b[0]))] for j in range(len(a))]
	for i in range(len(a)):
		for j in range(len(a[i])):
			for k in range(len(a[i])):
				#print(f'for {i},{j} adding {a[i][k] * b[k][j]},,,,j={j},k={k}')
				ans[i][j] += a[i][k] * b[k][j]
	return ans

if __name__ == '__main__':
	size = 3
	a = [[1,2,3],[4,5,6],[7,8,9]]
	b = [[5,7],[1,4],[9,8]]

	# print('a is -- ')
	# printf(a)
	# print('aT is ---')
	# at = transpose(a)
	# printf(at)

	# ans = product(a,at)

	# printf(ans)
	printf(transpose(a))
	printf(product(a,transpose(a)))