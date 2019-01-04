# proprietary to BEERA // DO NOT COPY

def fact(n):
	if n in [0,1]: return 1
	return n* fact(n-1)
if __name__ == '__main__':
	def process(i):
		if i in [0, 1]: return 1
		return (tim[i-1]*tim[n-1]) + process(n-1)
		# print(f'returning for {i-1} and {n-i}')
		# return process(i-1)*process(n-i)


	n 		=		int(input())
	tim		=		[0 for _ in range(n+1)]
	tim[0], tim[1]	=	1, 1
	# for i in range(n+1):
	# 	# tim[i] = (tim[i-1]*tim[n-1]) + tim[i-1]
	# 	tim[i]	=	process(i)
	# 	print(i,'---',tim)
	# print(tim)

	# print(tim[n])

	# for i in range(2, n+1):
	# 	tim[i]	=	(tim[i-1]*tim[i-i]) + tim[i-1]
	for i in range(1, n+1):
		ans = 0
		for j in range(1, i+1):
			ans += tim[j-1]*tim[i-j]
		tim[i] = ans

	print(tim[n]*fact(n))

