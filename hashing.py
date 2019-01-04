# proprietary to BEERA // DO NOT COPY



def hash_value(number):
	return (((((number*100)+8+10+94131-23142+231+123+235-75342)/20)*999)-32428*234)%1000


if __name__ == '__main__':
	phone_book = [-1 for _ in range(1001)]
	for _ in range(2):
		ph_no	=	int(input('Enter the phone number:\t'))
		h_value	=	hash_value(ph_no)
		phone_book[int(h_value)] = (input(f'Enter the nama for {ph_no}:\t'))
		print('hash value generated is',h_value)

	for _ in range(100):
		ph_no = int(input('Enter phone number to search:\t'))
		name = (phone_book[int(hash_value(ph_no))])
		if name == -1:
			print('Sorry, number not found')
			continue
		print('It belongs to',name)