# proprietary to BEERA // DO NOT COPY

#python3
from time import sleep

class phonebook():
	def __init__(self):
		self.dic = [[] for i in range(1000000)]

	def hash_int(self, x):
		a, b, p, m = 2354, 3125343, 10000271, 1000000
		return ((a*x+b)%p)%m

	def add(self, string):
		hash_, num, name = self.hash_int(int(string[1])), string[1], string[2]
		for i in range(len(self.dic[hash_])):
			if len(self.dic[hash_][i]) == 0: continue
			if self.dic[hash_][i][0] == string[1]:
				#print('chanign gnamr')
				#print('BEFORE:', self.dic[hash_][i])
				self.dic[hash_][i][1] = string[2]
				#print('AFTER:', self.dic[hash_][i])
				return
		self.dic[hash_].append([num, name])

	def find(self, string):
		hash_ = self.hash_int(int(string[1]))
		for contact in self.dic[hash_]:
			if len(contact) == 0: continue
			if contact[0] == string[1]:
				print(contact[1])
				return
		print('not found')

	def delete(self, string):
		hash_ = self.hash_int(int(string[1]))
		for i in range(len(self.dic[hash_])):
			if len(self.dic[hash_][i]) == 0: continue
			if self.dic[hash_][i][0] == string[1]:
				self.dic[hash_][i] = []
				return

	def process(self):
		n = int(input())
		for i in range(n):
			string = list(input().split())
			if string[0] == 'add':
				self.add(string)
			elif string[0] == 'find':
				self.find(string)
			elif string[0] == 'del':
				self.delete(string)
				

if __name__ == '__main__':
	ph = phonebook()
	ph.process()




