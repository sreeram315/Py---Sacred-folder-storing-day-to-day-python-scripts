# proprietary to BEERA // DO NOT COPY
import re


if __name__ == '__main__':
	string = '''Hello ji,
	I am Sreeram Maram, a very good boy,
	my ph no. 8919937557,
	email: sreerammmaram2@gmail.com,
		   sreerammaram@rocketmail.com,
		   sreerammaram1@gmail.com,
		   msreeram31@icloud.com,
		   gurubhaisemail@gmail.com,
	I am here to test regexes in python 3.7;
	thank you,
	Gurukanth Desai. hello
	Beera Singh Manant. Bye
	Abhinav Ram. Okay
	ram-123
	guru-456
	beera-789
	gadhar-089
	abhi-429
	132423
	012414
	901231wef
	111
	919
	1343
	666
	'''
	# 	l = re.findall('[a-z]+\w@\w+\.com',string)
	#	l = re.findall('\w+@\w+\.com',string)			# find emails
	# 	l = re.findall('sr.+',string)					# starts with
	#	l = re.findall('.*?[0-9]',string)				# greedy only one after '?'
	#	l = re.findall('.+;',string)					# end with		
	#	l = re.findall('\w+-(\d+)',string)				# group only ones in brackers, if more than one, tuples
	# 	l = re.findall('[100000-999999]{6}',string)
	#	l = re.findall(r'(\d)(?=\d\1)',string)			# the \1 here matches the firth parenthesis item, i.e. the thing in the first paranthesis should be next to next to it, with any nuber in the middle. matches: 989,212
	#	l = re.findall(r'(\d)(?=(?!\1)[0-9]\1)',string) # matches sames as above but doesnt match same number repeating 3 time like 111,000,999
	'''
	-->   .findall returns all the found patterns in a big string all through the string.
	-->   .match searches only at the start of a string and returns it, if found
	-->   .search serches all through the string and return the thing once its found and returns nothing
		          None if not found. Remember: It does NOT return all the matches, .findall does that
	'''

	l = re.findall(r'(\d)(?=(?!\1)[0-9]\1)',string)
	print(l)

