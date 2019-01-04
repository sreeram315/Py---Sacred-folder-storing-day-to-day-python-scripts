# proprietary to BEERA // DO NOT COPY



if __name__ == '__main__':
	no_of_people, no_of_queries, no_of_rows, queries, dic, answer	=	int(input()), int(input()), int(input()), [], {}, 1
	parent	=	[-1 for _ in range(no_of_people + 1)]
	met		=	[False for _ in range(no_of_people + 1)]
	arr		=	[[] for _ in range(no_of_people+1)]
	for _ in range(no_of_queries):
		a 	=	list(map(int, input().split()))
		queries.append(a)
	for query in queries:
		a, b = query[0], query[1]
		if (not met[a]) and (not met[b]):
			parent[a], parent[b] = a, a
			arr[a].append(b)
		elif (met[a] and (not met[b])) or (met[b] and (not met[a])):
			if met[a]:
				p 	=	parent[a]
				arr[p].append(b)
				parent[b] = a
			elif met[b]:
				p 	=	parent[b]
				arr[p].append(a)
				parent[a] = b
		elif met[a] and met[b]:
			arr[parent[a]] += arr[parent[b]]
			for i in arr[parent[b]]: parent[i] = parent[a]
			arr[parent[b]] = []
			arr[parent[a]].append(b)
		met[a], met[b] = True, True

	print(tree)
