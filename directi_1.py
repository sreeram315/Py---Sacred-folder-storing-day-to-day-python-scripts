# proprietary to BEERA // DO NOT COPY



if __name__ == '__main__':
	n , table, ans		=	int(input()), [], 0
	for _ in range(n): table.append(list(input().split('#')))
	pattern			=	str(input())
	passed_edges, passed_down_edges, passed_up_edges, passed_diagUP_edges, passed_diagDOWN_edges	=	[], [], [], [], []
	if len(pattern) == 0:
		print('0')
		exit()
	if len(pattern) == 1:
		count = 0
		for i in table:
			for j in i:
				if pattern == j:
					count += 1
		print(count)
		exit()

	def add(a1 ,b1 , a2, b2):
		ori		=	[[a1 ,b1] ,[a2, b2]]
		rev		=	[[a2 ,b2] ,[a1, b1]]
		if ori not in passed_edges and rev not in passed_edges:
			passed_edges.append(ori)
			return True
		return False


	def check_right(i, j):
		#print(f'len(table[i]) = {len(table[i])} and j = {j}')
		# try:
		if len(table[i])-j >= len(pattern):
			string	=	''
			for k in range(len(pattern)): string += table[i][j+k]
			if string == pattern:
				return add(i, j, i, j+k)
			return False
		# except:
		else:
			return False

	def check_down(i, j):
		# try:
		if len(table)-i >= len(pattern):
			string	=	''
			for k in range(len(pattern)): string += table[i+k][j]
			if string == pattern:
				return add(i, j, i+k, j)
			return False
		# except:
		else:
			return False

	def check_diagdown(i, j):
		# try:
		if len(table)-i >= len(pattern) and len(table[i])-j >= len(pattern):
			string = ''
			for k in range(len(pattern)): string += table[i+k][j+k]
			if string == pattern:
				return add(i, j, i+k, j+k)
			return False
		# except:
		else:
			return False

	def check_diagup(i, j):
		# try:
		if len(table[i])-j >= len(pattern) and  len(table)-i <= len(pattern):
			string = ''
			for k in range(len(pattern)): string += table[i-k][j+k]
			if string == pattern:
				return add(i, j, i-k, j+k)
			return False
		# except:
		else:
			return False


	for a in range(len(table)):
		for b in range(len(table[a])):
			i, j	=	a, b
			if check_right(i,j):
				#print(f'right for {i}, {j}')
				ans += 1
			if check_diagdown(i,j):
				#print(f'down for {i}, {j}')
				ans += 1
			if check_diagup(i,j):
				#print(f'diag up for {i}, {j}')
				ans += 1
			if check_down(i,j):
				#print(f'diag down for {i}, {j}')
				ans += 1
	# print(passed_up_edges)
	# print(passed_diag_edges)
	# print(passed_down_edges)
	print(ans)
	









	# for i in table:
	# 		for j in i:
	# 			print(j, end=' ')
	# 		print('')