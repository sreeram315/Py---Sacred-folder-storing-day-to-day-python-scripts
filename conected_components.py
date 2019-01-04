#python3 
# proprietary to BEERA // DO NOT COPY



class Maze(object):
	def __init__(self):
		self.nVertices, self.nEdges  = map(int, input().split())
		self.visited = [False for _ in range(self.nVertices + 1)]
		self.graph	=	[[0 for _ in range(self.nVertices + 1)] for j in range(self.nVertices + 1)]
		self.edges 	=	[list(map(int, input().split())) for _ in range(self.nEdges)]
		self.all_visits = []
		self.count 	=	0
		for lis in self.edges:
			l, m = lis[0], lis[1]
			self.graph[l][m], self.graph[m][l] = 1, 1
		# for i in range(1, self.nVertices + 1):
		# 	# print(i,'---',self.graph[i][1:])
		# print('\n\n')

	def explore(self, a):
		# print('Exploring',a)
		self.visited[a] = True
		for i in range(1, self.nVertices + 1):
			# print('LOOPING for ',i , self.graph[a][i])
			if not self.visited[i] and self.graph[a][i] == 1:
				# print('APPENDING',i)
				#self.all_visits.append(i)
				self.explore(i)
		return# self.all_visits

	def start_process(self):
		for i in range(1, self.nVertices + 1):
			if not self.visited[i]:
				# print('incrementing count for ',i)
				self.count += 1
				self.explore(i)
				# for j in range(len(self.visited)):
				# 	print(j,'----',self.visited[j])
				# print('\n')
		print(self.count)



if __name__ == '__main__':
	a 		=	Maze()
	a.start_process()


