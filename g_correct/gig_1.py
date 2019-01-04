# proprietary to BEERA // DO NOT COPY



if __name__ == '__main__':
	n, ultimate_sum, modulo, cost 	=	 int(input()), 0, (10**9)+7, []
	for i in range(n): cost.append(int(input()))
	cost_main = [0 for i in range(n)]
	cost_main[0] = cost[0]
	for i in range(1, n):
		cost_main[i]	= 	cost[i] + cost_main[i-1]
	for j in range(n):
		if j > 0: cost_sum	= [(cost_main[k] - cost_main[j-1]) for k in range(j, n)]
		else: cost_sum	= cost_main
		for i in range(len(cost_sum)):
			ultimate_sum += cost_sum[i]*cost[j+i]
	print(ultimate_sum % modulo)
	





















# if __name__ == '__main__':
# 	n 			= 3
# 	ultimate_sum, count = 0, n-1
# 	cost 		= [1, 2, 3]
# 	cost_main	= [sum(cost[:i+1]) for i in range(n)]
# 	cost_sum	= cost_main
# 	for j in range(n):
# 		try:
# 			if j > 0: cost_sum	= [(cost_main[k] - cost_main[j-1]) for k in range(j, n)]
# 			print(cost_sum)
# 		except:
# 			print('k=={},j=={}'.format(k,j))
# 	# 	for i in range(len(cost_sum)):
# 	# 		ultimate_sum += cost_sum[i]*cost[count]
# 	# 		print(cost_sum[i],'*',cost[count])
# 	# print(ultimate_sum)