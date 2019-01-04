# proprietary to BEERA // DO NOT COPY



class Hotel(object):
	def __init__(self):
		self.n 		=		int(input())
		self.timings	=		[]
		for i in range(self.n):
			string = list(input().split('#'))
			a, b = string[0], string[1]
			if a[-2:] == 'AM': a = int(a[:-2])
			else: a = int(a[:-2]) + 12
			if b[-2:] == 'AM': b = int(b[:-2])
			else: b = int(b[:-2]) + 12
			self.timings.append([a, b, b-a])

		self.timings.sort(key = lambda x: x[2])
		self.booking_hour	=	[0 for _ in range(24)]
		self.final_count 	=	0

	def available(self, a):
		# print('avalabeling for',a[0],a[1])
		for i in range(a[0], a[1]):
			if self.booking_hour[i] == 1:
				return False
		return True


	def start_process(self):
		# print(self.timings)
		for i in range(len(self.timings)):
			# print(f'checking for {self.timings[i]}')
			a = self.timings[i]
			if not self.available(a):
				# print('Failed for the same\n')
				continue
			# print('Upping for the same\n')
			for i in range(a[0], a[1]): self.booking_hour[i] = 1
			self.final_count += 1
			# print('bookings are', self.booking_hour)

	def print_result(self):
		print(self.final_count*500)



if __name__ == '__main__':
	a =	Hotel()
	a.start_process()
	a.print_result()







# if string[0][1] == 'A': string[0] = int(string[0][0])
# else: string[0] = int(string[0][0]) + 12
# if string[1][1] == 'A': string[1] = int(string[1][0])
# else: string[1] = int(string[1][0]) + 12

	
