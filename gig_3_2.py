# proprietary to BEERA // DO NOT COPY




if __name__ == '__main__':
	no_of_people, no_of_queries, no_of_rows, queries, dic, answer	=	int(input()), int(input()), int(input()), [], {}, 1
	arr	=	[]
	met	=	[0 for _ in range(no_of_people+1)]
	for _ in range(no_of_queries):
		a 	=	list(map(int, input().split()))
		queries.append(a)
	for query in queries:
		a, b = query[0], query[1]
		if met[a] == 0 and met[b] == 0:
			arr.append(set())
			arr[-1].add(a)
			arr[-1].add(b)
		elif met[a] != 0 and met[b] == 0:
			for i in range(len(arr)):
				if a in arr[i]: arr[i].add(b)
		elif met[a] == 0 and met[b] != 0:
			for i in range(len(arr)):
				if b in arr[i]: arr[i].add(a)
		# elif met[a] == 1 and met[b] == 1:
		# 	for i in range(len(arr)):
		# 		if a in arr[i]: f = i
		# 	for i in range(len(arr)):
		# 		if b in arr[i]: s = i
		# 	arr[f] += arr[s]
		# 	arr[s] = set([])
		met[a], met[b] = 1, 1


	for i in range(len(arr)):
		answer *= len(arr[i])

	print(answer)

