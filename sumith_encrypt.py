# proprietary to BEERA // DO NOT COPY

import pandas as pd

def encrypt(message, number = ''):
		for let in message:
			if let == ' ':
				number += '0 '
				continue
			a = ord(let)
			a += 8
			number += str(int(a)) + ' '
		answer, ans = '', ''
		for num in number.split(' '):
			if num == '0':
				ans += '$$$ '
				continue
			for i in range(0, len(num), 2):
				if len(num[i:]) == 3:
					ans += chr(int(num[i:i+3]))
					break
				ans += chr(int(num[i:i+2]))
			ans += ' '
		save(message, ans)
		return ans

def decrypt(message, answer = '', numbers = ''):
		for ans in message.split(' '):
			if ans == '$$$':
				numbers += '0 '
				continue
			for let in ans:
				numbers += str(ord(let))
			numbers += ' '
		
		numbers = [num for num in numbers.split()]

		for number in numbers:
			if number == '0':
				answer += ' '
				continue
			number = int(number)
			number -= 8
			answer += chr(int(number))
		return answer

def save(string, answer):
		df = pd.read_csv('sumith_list.csv')
		df = df.append({'Message': string, 'Encryped format': answer}, ignore_index = True)
		df.to_csv('sumith_list.csv')
		print('Saved in database. Thank you.')


def main():
	while True:
		print('''\t\tWELCOME TO BEERA ENCRYPTOR AND DECRYPTOR
			1.Encryptor
			2.Decryptor
			3.END
			''')
		option = int(input())

		if option ==1:
			string = input('Enter the message:\t')
			print('Your encryped message is ', encrypt(string))
		elif option == 2:
			string = input('Enter the encrypted message:\t')
			print('Your decrypted message is',decrypt(string))
		elif option == 3:
			exit()
		else:
			print('Wrong option choosen.')


main()
exit()


































