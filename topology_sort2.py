#python3 
# proprietary to BEERA // DO NOT COPY

class Topology():
	def __init__(self):
		self.no_of_vertices, self.no_of_edges	=	map(int, input().split())
		self.graph = [[] for _ in range(self.no_of_vertices + 1)]
		for _ in range(1, self.no_of_edges + 1):
			a, b = map(int, input().split())
			if b not in self.graph[a]: self.graph[a].append(b)
		self.visited = [False for _ in range(self.no_of_vertices + 1)]
		self.pre_order = [0 for _ in range(self.no_of_vertices + 1)]
		self.post_order = [0 for _ in range(self.no_of_vertices + 1)]
		self.order = 1

	def explore(self, k):
		self.visited[k] = True
		self.pre_order[k] = self.order
		self.order += 1
		# print('processing', k)
		for edge in self.graph[k]:
			if not self.visited[edge]:
				self.explore(edge)
		self.post_order[k] = self.order
		self.order += 1


	def dfs(self):
		for i in range(1, self.no_of_vertices + 1):
			if not self.visited[i]:
				self.explore(i)
		#print(self.pre_order)
		return self.post_order

if __name__ == '__main__':
	a = Topology()
	ans = a.dfs()
	#print(ans)
	dic = []
	for i in range(1, len(ans)):
		dic.append([i,ans[i]])
	dic.sort(key = lambda x: x[1])
	dic.reverse()
	for i in dic: print(i[0], end = ' ')





