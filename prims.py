from collections import defaultdict
import heapq


def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst


import sys
sys.stdin = open("ii.txt")
# Kruskal's algorithm i

n = int(input())
e = int(input())

edges = []
for i in range(e):
    edges.append(input())



example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

g = {}

for i in range(1, n+1):
    g[i] = {}
for edge in edges:
    e1, e2, w = int(edge.split()[0]), int(edge.split()[1]), int(edge.split()[2])
    g[e1][e2] = w
    g[e2][e1] = w
print(g)


print(dict(create_spanning_tree(g, 1)))
