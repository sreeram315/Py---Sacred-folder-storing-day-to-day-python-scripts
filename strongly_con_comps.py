#python3 
# proprietary to BEERA // DO NOT COPY
import sys
sys.setrecursionlimit(200000)

class SSC():
	def __init__(self):
		self.no_of_vertices, self.no_of_edges	=	map(int, input().split())
		self.graph = [[] for _ in range(self.no_of_vertices + 1)]
		self.ograph = [[] for _ in range(self.no_of_vertices + 1)]
		for _ in range(1, self.no_of_edges + 1):
			b, a = map(int, input().split())
			if b not in self.graph[a]: self.graph[a].append(b)
			if a not in self.ograph[b]: self.ograph[b].append(a)
		self.visited = [False for _ in range(self.no_of_vertices + 1)]
		self.pre_order = [0 for _ in range(self.no_of_vertices + 1)]
		self.post_order = [0 for _ in range(self.no_of_vertices + 1)]
		self.order = 1

	def explore(self, k):
		self.visited[k] = True
		self.pre_order[k] = self.order
		self.order += 1
		#print('processing', k)
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
		#print(self.post_order)

	def explore1(self, k):
		#print('exploring ',k, 'which has ',self.ograph[k])
		ans = []
		ans.append(k)
		self.visited[k] = True
		self.pre_order[k] = self.order
		self.order += 1
		#print('processing', k)
		for edge in self.ograph[k]:
			if not self.visited[edge]:
				#print('brace',edge)
				#print(f'ans = {ans}, edge = {edge}')
				ans  += self.explore1(edge)
		self.post_order[k] = self.order
		self.order += 1
		return ans


	def start_process(self):
		self.visited = [False for _ in range(self.no_of_vertices + 1)]
		ans = []
		#print('post order = ',self.post_order)
		l = [i[0] for i in sorted(enumerate(self.post_order), key=lambda x:x[1])]
		l.reverse()
		#print('l = ',l)
		for i in l:
			if i == 0: continue
			if not self.visited[i]:
				#print('----------------')
				a = self.explore1(i)
				#print('a = ',a)
				ans.append(a)
				#print('final = ',ans)
		print(len(ans))
		

if __name__ == '__main__':
	a = SSC()
	a.dfs()
	a.start_process()
