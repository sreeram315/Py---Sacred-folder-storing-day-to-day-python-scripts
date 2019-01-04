# proprietary to BEERA // DO NOT COPY
#python3


import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size



class IsBinaryTree():
	def read(self):
		self.n = int(sys.stdin.readline())
		self.key	=	[0 for i in range(self.n)]
		self.left 	=	[0 for i in range(self.n)]
		self.right	=	[0 for i in range(self.n)]
		self.result	=	[]
		self.is_root= 	[None for _ in range(self.n)]
		for i in range(self.n):
			[a, b, c] = map(int, sys.stdin.readline().split())
			self.key[i] = a
			self.left[i] = b
			self.right[i] = c
		if self.n <= 1:
			print('CORRECT')
			exit()

	def in_order(self, N):
		if self.left[N] == -1 and self.right[N] == -1:
			self.result.append(self.key[N])
			self.is_root[N] = False
			return
		if self.left[N] != -1: self.in_order(self.left[N])
		self.result.append(self.key[N])
		self.is_root[N] = True
		if self.right[N] != -1: self.in_order(self.right[N])
		return self.result


	def is_binary_tree(self, N):
		arr	=	self.in_order(0)
		#print(arr)
		#print(self.is_root)
		if all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)):
			for N in range(self.n):
				if self.left[N] != -1 and self.key[N] == self.key[self.left[N]]:
					#print(f'conparing {self.key[N]} and {self.key[self.left[N]]}')
					return False
			return True


		# returns a bool saying it is a binary tree or not




def main():
	B 	=	IsBinaryTree()
	B.read()
	if B.is_binary_tree(0): print('CORRECT')
	else:print('INCORRECT')

threading.Thread(target=main).start()













