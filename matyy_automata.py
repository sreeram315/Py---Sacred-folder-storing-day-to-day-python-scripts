


def multyply(a, b):
	rows = len(a)
	columns = len(b[0])
	mat = [[0 for i in range(columns)] for j in range(rows)]

	for i in range(len(mat)):
		for j in range(len(mat[i])):
			for k in range(len(a[0])):
				mat[i][j] += a[i][k]*b[k][j]

	return mat

def tt(rows, columns, fir):
	mat = [[0 for i in range(columns)] for j in range(rows)]
	mat_T = [[0 for i in range(rows)] for j in range(columns)]

	for i in range(len(mat)):
		for j in range(len(mat[i])):
			mat[i][j] = fir
			fir += 1
	print(mat)

	for i in range(len(mat_T)):
		for j in range(len(mat_T[i])):
			mat_T[i][j] = mat[j][i]

	print(mat_T)

	ans = multyply(mat, mat_T)
	print(ans)
	for i in ans:
		for j in i:
			print(j, end= ' ')
		print('')


if __name__ == '__main__':
	rows = 3
	columns = 3
	fir = 1
	print(tt(rows, columns, fir))