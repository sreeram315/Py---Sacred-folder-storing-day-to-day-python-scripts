# proprietary to BEERA // DO NOT COPY



if __name__ == '__main__':
	no_of_people, no_of_queries, no_of_rows, queries, dic, answers	=	int(input()), int(input()), int(input()), [], {}, []
	parent	=	[None for _ in range(no_of_people + 1)]
	met		=	[False for _ in range(no_of_people + 1)]
	arr		=	[[] for _ in range(no_of_people+1)]
	for _ in range(no_of_queries):
		a 	=	list(map(int, input().split()))
		queries.append(a)
	for query in queries:
		a, b = query[0], query[1]
		#print(f'LOOP WITH a={a} and b={b}')
		if (not met[a]) and (not met[b]):
			parent[a], parent[b] = a, a
			arr[a].append(b)
		elif met[a] and (not met[b]):
			p 	=	parent[a]
			arr[p].append(b)
			parent[b] = p
		elif met[b] and (not met[a]):
			p 	=	parent[b]
			arr[p].append(a)
			parent[a] = p
		elif met[a] and met[b]:
			i, j = parent[a], parent[b]
			if i == j: continue
			arr[i] += arr[j]
			arr[i].append(j)
			for item in arr[j]: parent[item] = i
			parent[j] = i	
			arr[j] = []
		else:
			print('WTF')
			exit()
		met[a], met[b] = True, True
		#print('parent ----- ',parent)
		#print(arr,'\n\n')
	#print(arr)
	for item in arr:
		if len(set(item)) == 0: continue
		answers.append(len(set(item))+1)
	#print(answers)
	prod 		=		0
	for i in range(len(answers)):
		prod += answers[i]*sum(answers[i+1:])
	print(prod)
