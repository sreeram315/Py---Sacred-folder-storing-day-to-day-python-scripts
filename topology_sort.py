#python3
# proprietary to BEERA // DO NOT COPY
#python3


class cyclic_dependecy_check():
	def __init__(self):
		self.no_of_vertices, self.no_of_edges	=	map(int, input().split())
		self.graph = [[] for _ in range(self.no_of_vertices + 1)]
		for _ in range(1, self.no_of_edges + 1):
			a, b = map(int, input().split())
			if b not in self.graph[a]: self.graph[a].append(b)
		#for i in range(1, len(self.graph)):
		#	print(i,'--',self.graph[i])
		self.visited = [False for _ in range(self.no_of_vertices + 1)]
		self.done = [False for _ in range(self.no_of_vertices + 1)]
		self.final_answer = []
		self.visits = [[] for _ in range(self.no_of_vertices + 1)]

	def reaches(self, i ):
		ans = []
		#print('doing reachers for ',i)
		for edge in self.graph[i]:
			#print('edge = ',edge, 'i = ',i)
			if not self.visited[edge]:
				self.visited[edge] = True
				#print(f'adding {edge} to {ans} because of {i}')
				ans.append(edge)
				ans += self.reaches(edge)
		return ans

	def remove_re(self, k):
		for i in range(1, self.no_of_vertices + 1):
			try:
				self.visits[i].remove(k)
			except:
				pass

	def start_processs(self):
		for i in range(1, self.no_of_vertices + 1):
			if self.done[i]: continue
			#print('----------------',i,'----------------')
			self.visited = [False for _ in range(self.no_of_vertices + 1)]
			a = self.reaches(i)
			#print(f'reachers of {i} is {a}')
			if len(a) == 0:
				self.final_answer.append(i)
				self.remove_re(i)
				self.done[i] = True
				self.start_process()
		return self.final_answer

	def start_process(self):
		for i in range(1, self.no_of_vertices + 1):
			self.visited = [False for _ in range(self.no_of_vertices + 1)]
			a = self.reaches(i)
			self.visits[i] = a

		
		dcount = 0
		dvertices = []
		ans = []

		while dcount < self.no_of_vertices:
			for i in range(1, self.no_of_vertices + 1):
				if (i not in dvertices) and (len(self.visits[i]) == 0):
					ans.append(i)
					dvertices.append(i)
					self.remove_re(i)
					dcount += 1
					break
		return ans




if __name__ == '__main__':
	a = cyclic_dependecy_check()
	ans = a.start_process()
	ans.reverse()
	for i in ans: print(i, end=' ')


		