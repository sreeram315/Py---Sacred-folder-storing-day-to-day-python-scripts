# proprietary to BEERA // DO NOT COPY
#python3



"""def tree_depth(root):
	global count
	count+=1
	print('count==',count)
	print(root)
	
	print('DONE==',done)
	if root not in arr:
		print('***************')
		return 1
	m =  1 + max(map(tree_depth, [index for index, value in enumerate(arr) if (value == root) ] ))
	done.append(root)
	return m"""



def tree_depth2(dic, root, n):
	level = [0] * n
	level[root] = 1
	visited = [False] * len(arr)
	q = []
	q.append(root)
	visited[root] = True
	while q:
		s = q.pop(0)
		#print('s==',s)
		for i in dic[s]:
			if visited[i] == False:
				level[i] = 1 + level[s]
				visited[i] = True
				q.append(i)
				last = i
	return level[last]

input()
arr = list(map(int, input().split()))
dic = [[]for i in range(len(arr))]
for i in range(len(arr)):
	if arr[i] == -1: root = i
	dic[arr[i]].append(i)
print(tree_depth2(dic, root, len(arr)))

