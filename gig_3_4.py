# proprietary to BEERA // DO NOT COPY



if __name__ == '__main__':
	no_of_people, no_of_queries, no_of_rows, queries, dic, answer	=	int(input()), int(input()), int(input()), [], {}, 1
	queries 		=	[list(map(int, input().split())) for _ in range(no_of_queries)]
	is_childnode	=	[None for _ in range(no_of_people+1)]
	is_parentnode	=	[None for _ in range(no_of_people+1)]
	parent 			=	[None for _ in range(no_of_people+1)]
	met				=	[False for _ in range(no_of_people+1)]
	tree			=	[[] for _ in range(no_of_people + 1)]
	count 			=	0

	for query in queries:
		a, b			=	query[0],	query[1]
		#print(f'Loop { count } for {a}, {b}')
		count += 1
		if a==b: continue
		if (met[a] and not( met[b])) or (met[b] and (not met[a])):
			if is_childnode[a]:
				p 			=	parent[a]
				#print(tree[p], b)
				tree[p].append(b)
				parent[b]	=	p
				is_childnode[b]	=	True
			elif is_childnode[b]:
				p 			=	parent[b]
				tree[p].append(a)
				parent[a]	=	p
				is_childnode[a]	=	True
			elif is_parentnode[a]:
				tree[a].append(b)
				is_childnode[b]	=	True
				parent[b]		=	a
			elif is_parentnode[b]:
				tree[b].append(a)
				is_childnode[a]	=	True
				parent[a]		=	b
		elif (not met[a]) and (not met[b]):
			is_parentnode[a]	=	True
			is_childnode[b]		=	True
			parent[b]			=	a
			tree[a].append(b)
		elif met[a] and met[b]:
			if not(parent[a]==b or parent[b]==a):
				#print('MERGER FOR ',a,'and',b)
				if is_childnode[a]: i = parent[a]
				else: i = a
				if is_childnode[b]: j = parent[b]
				else: j = b
				if (i != j):
					#print('joining ',i,j)
					tree[i] += tree[j]
					tree[i].append(j)
					for item in tree[j]:
						parent[item] = i
					tree[j]	=	[]
					is_childnode[j]	=	True
					parent[j]	=	i
		met[a], met[b]	=	True, True
		#print(tree,'\n\n')
	#print('\n\nOUT OFF LOOP\n\n')
	#print(tree)
	answer	=	[]
	####################
	unused, used = 0, 0
	for bul in met[1:]:
		if not bul:
			unused += 1
		else:
			used += 1
	#print('Unused = ',unused)
	#print('Used = ',used)
	among_unused	=	int((unused*(unused-1))/2)

	#####################
	for i in range(len(tree)):
		if len(tree[i]) == 0: continue
		count	=	len(set(tree[i]))
		if i not in set(tree[i]): count += 1
		answer.append(count)
	product	=	0
	#print(answer)
	if len(answer) == 0:
		if unused == 0:
			print('0')
			exit()
		else:
			print(among_unused)
			exit()
	if len(answer) == 1:
		l = len(answer[0])
		unused_with_used	=	unused * l
		print(unused_with_used + among_unused)
		exit()

	for num in answer:
		if product == 0: product = num
		else:
			product *=	num
	

	unused_with_used	=	int(used * unused)
	#print('Unused = ',unused)
	#print('Used = ',used)
	#print('Among unused', among_unused)
	#print('Unised with used', unused_with_used)
	print(int(product + unused_with_used + among_unused))




