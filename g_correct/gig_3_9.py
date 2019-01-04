
# proprietary to BEERA // DO NOT COPY


if __name__ == '__main__':
	def get_root(a):
		while root[str(a)] != -1: a 	=	root[str(a)]
		return str(a)
	no_of_people, no_of_queries, no_of_rows, queries, dic, answer	=	int(input()), int(input()), int(input()), [], {}, 1
	root	=	{}
	met	=	[False for _ in range(no_of_people+1)]
	queries 	=	[list(map(int, input().split())) for _ in range(no_of_queries)]
	count = 0
	for query in queries:
		count += 1
		a, b = query[0], query[1]
		#print(f'Loop {count} wiht {a} and {b}')
		if (not met[a]) and (not met[b]):
			dic[str(a)]			=	2
			root[str(a)]		=	-1
			root[str(b)]		=	str(a)
		elif (met[a] and (not met[b])):
			p 	=	get_root(a)
			dic[str(p)] += 1
			root[str(b)]	=	str(p)
		elif (met[b] and (not met[a])):
			p 	=	get_root(b)
			dic[str(p)] += 1
			root[str(a)]	=	str(p)
		elif met[a] and met[b]:
			i, j	=	get_root(a), get_root(b)
			if i == j: continue
			dic[str(i)] += dic[str(j)]
			root[str(j)]	=	str(i)
			del dic[str(j)]
		met[a], met[b]	=	True, True
		#print(f'After loop dic = {dic}')
		#print(f'After loop root = {root}\n\n')

	answers = list(dic.values())
	#print(f'answers = {answers}\n')
	prod = answers[0]
	for i in range(1, len(answers)):
		prod *= answers[i]

	print(prod)
	






