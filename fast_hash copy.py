# proprietary to BEERA // DO NOT COPY
#python3
from time import sleep

class hashers(object):
	def __init__(self):
		self.no_of_buckets = int(input())
		self.no_of_quiries = int(input())
		self.dic = [[] for i in range(self.no_of_buckets)]

	def hashvalue(self, word):
		x, p, m = 263, 1000000007, self.no_of_buckets
		power, summ = 0, 0
		word = [ord(letter) for letter in word]
		for letter in word:
			summ += letter*(x**power)
			power += 1
		return (summ%p)%m

	def add(self, string):
		hash_ = self.hashvalue(string[1])
		if string[1] not in self.dic[hash_]:
			self.dic[hash_].insert(0, string[1])  # if time overloads revrse this

	def check(self, string):
		hash_ = int(string[1])
		if len(self.dic[hash_]) == 0:
			print('')
			return
		for word in self.dic[hash_]: print(word+' ', end ='')
		print('\n',end='')

	def find(self, string):
		hash_ = self.hashvalue(string[1])
		if string[1] in self.dic[hash_]: print('yes')
		else: print('no')

	def delete(self, string):
		hash_ = self.hashvalue(string[1])
		if string[1] in self.dic[hash_]:
			self.dic[hash_].remove(string[1])

	def startprocess(self):
		for quiry in range(self.no_of_quiries):
			string = list(input().split())
			if string[0] == 'add': self.add(string)
			elif string[0] == 'check': self.check(string)
			elif string[0] == 'find': self.find(string)
			elif string[0] == 'del': self.delete(string)
			else: print('UNKNOWN EXCEPTION OCCURED, BAD INPUT')


if __name__ == '__main__':
	pb = hashers()
	pb.startprocess()
	

