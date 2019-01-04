# proprietary to BEERA // DO NOT COPY



if __name__ == '__main__':
	no_of_people, no_of_queries, no_of_rows, queries, dic, answer	=	int(input()), int(input()), int(input()), [], {}, 1
	done = [False for i in range(no_of_people)]
	met	=	[0 for _ in range(no_of_people+1)]
	queries 	=	[list(map(int, input().split())) for _ in range(no_of_queries)]
	for query in queries:
		a, b = query[0], query[1]
		if is_childnode[a]:
			p 	=	parent[a]
			tree[str(p)].append(b)
			is_childnode[b] = True
			parent[b]	=	p
		elif not is_childnode[a]:		#CHECK
			dic[str(a)]	=	[a,b]
			is_childnode[b]	=	True
			parent[b]	=	a



