# proprietary to BEERA // DO NOT COPY
#python3
from time import sleep
from collections import defaultdict


class phonebook():
	def __init__(self):
		self.num_to_name = defaultdict(lambda: 'not found')
		self.name_to_num = defaultdict(lambda: 'not found')

	def add(self, num, name):
		self.num_to_name[num] = name
		self.name_to_num[name] = num

	def delete(self, num):
		try:
			del self.name_to_num[self.num_to_name[num]]
			del self.num_to_name[num]
		except:
			pass
		

	def find(self, num):
		print(self.num_to_name[num])

	def start_process(self):
		n = int(input())
		for i in range(n):
			string = list(input().split())
			if string[0] == 'add': self.add(string[1], string[2])
			elif string[0] == 'find': self.find(string[1])
			elif string[0] == 'del': self.delete(string[1])

if __name__ == '__main__':
	ph = phonebook()
	ph.start_process()







