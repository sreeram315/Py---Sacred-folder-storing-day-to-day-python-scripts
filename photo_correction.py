



if __name__ == '__main__':
	handle = open('all_girsl_ids.txt', 'r')
	ids = handle.readlines()[0].split(' ')

	for reg in ids:
		try:
			handle = open(f'images_lpu/girls_data/{reg}.png')
		except:
			print(reg)