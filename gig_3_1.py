# proprietary to BEERA // DO NOT COPY









if __name__ == '__main__':
	def incrementby(a, b):
		print('incrementing',a)
		while (arr[a] != -1):
			a 	=	arr[a]
		dic[str(a)]	+= int(b)

	no_of_people, no_of_queries, no_of_rows, queries, dic, answer	=	int(input()), int(input()), int(input()), [], {}, 1
	arr		=	[0 for _ in range(no_of_people+1)]
	for _ in range(no_of_queries):
		a 	=	list(map(int, input().split()))
		queries.append(a)
	for query in queries:
		a, b = query[0], query[1]
		if (arr[a] == 0) and (arr[b] == 0):
			arr[a] +=	-1
			try:	dic[str(a)] += 2
			except: dic[str(a)]  = 2
			arr[b]	=	a
		elif (arr[a] != -1 and arr[a] != 0) and (arr[b] == 0):
			incrementby(a, 1)
			arr[b]  =   a
		elif (arr[a] == 0) and (arr[b] == -1):
			incrementby(b, 1)
			arr[a]	=	b
	for value in dic.values():
		answer *= value
	print(dic)
	modulo	=	(10**9)+7
	print(answer%modulo)

