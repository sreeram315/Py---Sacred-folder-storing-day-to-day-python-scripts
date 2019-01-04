# proprietary to BEERA // DO NOT COPY



class Society():
	def __init__(self):
		self.no_of_people, self.no_of_queries, self.no_of_rows, self.queries, self.dic, self.answer	=	int(input()), int(input()), int(input()), [], {}, 1
		self.queries 			=	[list(map(int, input().split())) for _ in range(self.no_of_queries)]
		self.is_childnode		=	[None for _ in range(self.no_of_people+1)]
		self.is_parentnode		=	[None for _ in range(self.no_of_people+1)]
		self.parent 			=	[None for _ in range(self.no_of_people+1)]
		self.met				=	[False for _ in range(self.no_of_people+1)]
		self.tree				=	[[] for _ in range(self.no_of_people + 1)]
		self.count 				=	0
		self.used, self.unused	=	0, 0
		self.answers			=	[]
		self.debug				=	True
		self.with_unused		=	0		###
		self.among_used 		=	0		###
		self.modulo				=	(10**9)+7
		#print('OUT OFF INPUT')


	def one_met(self, a, b):
		if self.is_childnode[a]:
			p 							=	self.parent[a]
			self.tree[p].append(b)
			self.parent[b]				=	p
			self.is_childnode[b]		=	True
		elif self.is_childnode[b]:
			p 							=	self.parent[b]
			self.tree[p].append(a)
			self.parent[a]				=	p
			self.is_childnode[a]		=	True
		elif self.is_parentnode[a]:
			self.tree[a].append(b)
			self.is_childnode[b]		=	True
			self.parent[b]				=	a
		elif self.is_parentnode[b]:
			self.tree[b].append(a)
			self.is_childnode[a]		=	True
			self.parent[a]				=	b
		return

	def no_met(self, a, b):
		self.is_parentnode[a]			=	True
		self.is_childnode[b]			=	True
		self.parent[b]					=	a
		self.tree[a].append(b)
		return

	def both_met(self, a, b):
		i, j			=		None, None
		if (self.parent[a]==b or self.parent[b]==a): return
		###########################
		if self.is_childnode[a]: 	i 			= self.parent[a]
		elif self.is_parentnode[a]: i 			= a
		if self.is_childnode[b]: 	j 			= self.parent[b]
		elif self.is_parentnode[b]: j 			= b
		###########################
		if i == j: return
		self.tree[i] 									+=  self.tree[j]
		self.tree[i].append(j)
		for item in self.tree[j]: self.parent[item] 	=   i
		self.tree[j]									=	[]
		self.is_childnode[j]							=	True
		self.parent[j]									=	i
		return

	def get_used_and_unused(self):
		u, unu 		=		0, 0
		for bul in self.met[1:]:
			if not bul: unu += 1
			else:  		u   += 1
		return u, unu

	def get_answers(self):
		ans 		=		[]
		for i in range(1, len(self.tree)):
			if len(self.tree[i]) == 0: continue
			count 		=		len(set(self.tree[i]))
			if i not in set(self.tree[i]): count += 1
			ans.append(count)
		return ans

	def check_empty_answers(self):
		if len(self.answers) > 0: return
		if self.unused == 0:	print('0')
		else:	print(self.with_unused)
		exit()

	def check_only_one_answer(self):
		if len(self.answers) != 1: return
		l 	=	int(self.answers[0])		###
		print(self.with_unused)
		exit()

	def get_among_used(self):
		prod 		=		0
		for i in range(len(self.answers)):
			for j in range(i+1, len(self.answers)):
				prod += self.answers[i]*self.answers[j]
		return prod

	def get_among_unused(self):
		among_unu 	=	int(((self.unused)*(self.unused-1))/2)
		unu_with_u	=	self.unused * self.used
		return int(among_unu + unu_with_u)

	def start_process(self):
		#Looping through all the queries
		count = 0
		for query in self.queries:
			a, b 	=	query[0], 	query[1]
			if a == b: continue
			if (self.met[a] and not( self.met[b])) or (self.met[b] and (not self.met[a])):
				self.one_met(a, b)
			elif (not self.met[a]) and (not self.met[b]):
				self.no_met(a, b)
			elif self.met[a] and self.met[b]:
				self.both_met(a, b)
			self.met[a], self.met[b]	=	True, True
			count += 1
			

		self.used, self.unused	=	self.get_used_and_unused()
		self.answers			=	self.get_answers()

		self.among_used 				=	self.get_among_used()		###
		self.with_unused				=	self.get_among_unused()		###


		self.check_empty_answers()
		self.check_only_one_answer()

		

		print(int(self.among_used)%self.modulo)


		


if __name__ == '__main__':
	a 		=		Society()
	a.start_process()
