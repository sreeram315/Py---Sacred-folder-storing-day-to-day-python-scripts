import sys
sys.stdin = open('dyk_input.txt', 'r')
sys.stdout = open('dyk_output.txt', 'w+')

def get_node(cost, done):
	s = list(zip(cost, done, [i for i in range(len(cost))]))
	s.sort(key = lambda x: x[0])
	# print(s)
	for tup in s:
		if not tup[1]:
			return tup[2]




def dyk(arr):
	done = [0 for _ in range(len(arr))]
	cost = [9999999999999 for _ in range(len(arr))]
	cost[0] = 0
	i = 0

	while(any(done[k]==0 for k in range(len(arr)))):
		node = get_node(cost, done)
		# print('got node', node)
		for adj in range(len(arr[node])):
			if arr[node][adj] == 0: continue
			new_dist = cost[node] + arr[node][adj]
			old_dist = cost[adj]
			# print(f'new = {new_dist} old = {old_dist}')
			if new_dist < old_dist:
				cost[adj] = new_dist
		done[node] = 1


	print("Node\t\tShortest Distance")
	for i in range(len(cost)):
		print(f" {i+1}\t\t\t\t{cost[i]}")
	exit()






def main():
	rows = int(input())
	arr = []

	for i in range(rows):
		arr.append(list(map(int, input().split())))
	
	# for i in range(len(arr)):
	# 	print(arr[i])

	dyk(arr)

def main2():
	cost = [4,6,1,6,8,3]
	done = [0,0,1,0,0,0]
	print(get_node(cost, done))





main()