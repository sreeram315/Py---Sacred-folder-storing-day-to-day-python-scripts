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
		self.visited = [False for _ in range(self.no_of_edges + 1)]

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



	def start_process(self):
		for i in range(1, self.no_of_vertices + 1):
			#print('----------------',i,'----------------')
			self.visited = [False for _ in range(self.no_of_vertices + 1)]
			a = self.reaches(i)
			#print(f'reachers of {i} is {a}')
			if i in a:
				#print(i, a)
				print('1')
				exit()
		print('0')
		exit()


if __name__ == '__main__':
	a = cyclic_dependecy_check()
	a.start_process()


		