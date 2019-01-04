# import pandas as pd 



# def encrypt(string):
# 	encrypted = ''
# 	for let in string:
# 		a = ord(let)
# 		a 	=	((((a*21)/123)+3)*20913)
# 		encrypted += str(a)
# 	return encrypted
		
# def add_new_email():

# def check_pass():

# def view_data():
# 	df 	=	pd.read_csv('Bhanu_Password.csv')
# 	print(df)
# 	exit()


# if __name__ == '__main__':
# 	print('''\t\t\t Welcome to Bhanu Encryption System
# 				Select any one:
# 				1)\t Add new email and password.
# 				2)\t Check if password is correct or not.
# 				3)\t View all data
# 		''')
# 	option	=	int(input())
# 	if option == 1: add_new_email()
# 	if option == 2: check_pass()
# 	if option == 3: view_data()
# 	else:
# 		print('Wrong option selected')


# 	df = pd.read_csv('Bhanu_Pbassword.csv')
# 	email = input('Enter an email')
# 	string = input('Enter a Password')
# 	encryped_password	=	encrypt(string)
# 	df.append({'Username': email, 'Password': encryped_password}, ignore_index = True)
