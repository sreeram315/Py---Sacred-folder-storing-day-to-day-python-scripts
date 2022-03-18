
import sys
sys.stdin = open("ii.txt")
# Kruskal's algorithm in Python


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([min(u,v)+1, max(u,v)+1, w])
                self.apply_union(parent, rank, x, y)
        w = 0
        for x in result:
            w += x[2]
        print(w)

    def prims_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([min(u,v)+1, max(u,v)+1, w])
                self.apply_union(parent, rank, x, y)
        w = 0
        for x in result:
            w += x[2]
        print(w)


n = int(input())
g = Graph(n)
e = int(input())

edges = []
for i in range(e):
    edges.append(input())




for edge in edges:
    e1, e2, w = int(edge.split()[0])-1, int(edge.split()[1])-1, int(edge.split()[2])
    g.add_edge(e1, e2, w)

g.kruskal_algo()
g.prims_algo()
# dic = {}
# for i in range(1, n+1):
#     dic[i] = []
# for x in result:
#     dic[x[0]].append(x[1])
#     dic[x[1]].append(x[0])
# print(dic)

# reached = [1]
# print(1, end = ' ')
# while(len(reached) != n):
#     for x in dic[reached[-1]]:
#         if x not in reached:
#             print(x, end = ' ')
#             reached.append(x)



# print(1, end = ' '); node = 1
# while(node != n):
#     for x in result:
#         print(if )






