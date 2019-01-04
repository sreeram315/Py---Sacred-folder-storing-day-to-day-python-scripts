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
		if met[a]==False and met[b]==False:
			arr.append([a, b])
		elif met[a]==True and met[b]==False:
			for i in range(len(arr)):
				if a in arr[i]:
					arr[i].append(b)
					break
		elif met[b]==True and met[a]==False:
			for i in range(len(arr)):
				if b in arr[i]:
					arr[i].append(a)
					break
		elif met[a]==True and met[b]==True:
			for k in range(len(arr)):
				if a in arr[k]: i = k
				if b in arr[k]: j = k
			if i == j: continue
			arr[i] += arr[j]
			arr[j]	=	[]
		met[a], met[b]	=	True, True
	for item in arr:
		if len(set(item)) == 0: continue
		answers.append(len(set(item)))
	prod 		=		0
	for i in range(len(answers)-1):
		prod += answers[i]*sum(answers[i+1:])


	u, unu = 0,0 
	for bul in met[1:]:
		if bul == True: u += 1
		else: unu += 1

	among_unused	=	(unu*(unu-1))/2
	unu_with_u		=	unu*u
	
	print(int(prod + unu_with_u))






