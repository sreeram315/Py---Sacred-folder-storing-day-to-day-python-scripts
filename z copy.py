import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
string1 = '1bboH68phURr8xI4AE4clc404jTUfzMXQc3JzkpakKQaegy8p0bb0p8ygeaQKkapkzJ3cQXMzfUTj404clc4EA4Ix8rRUhp86HobbktUWFJGOJTeGUemLBIpMW4eyFUGlx42THdjhUea4RpIViCUGm5OO5mGUCiVIpR4aeUhjdHT24xlGUFye4WMpIBLmeUGeTJOGJFWUtm8kGWlsxzTOd38fhqOEYdO2FM5QZu4fyjzzwrIu9EL1KHgfqmvGGvmqfgHK1LE9uIrwzzjyf4uZQ5MF2OdYEOqhf83dOTzxslWGk873jsZ3LqJHpQO0MKTcbxPgmHi2kCDt0XlCFk6XOrSGiuBt6JMFKKFMJ6tBuiGSrOX6kFClX0tDCk2iHmgPxbcTKM0OQpHJqL3Zsj3pbknAo6Go7MrpPZdpt1TjuQTS7UQw8N8ZOZJrEcyDHsGU7mhbMaaMbhm7UGsHDycErJZOZ8N8wQU7STQujT1tpdZPprM7oG6oAnkbwnLNQtCU6VY1H2ayWMjZGE1EapWO8iVHGXdHFsCfZ5PAzL4g3LvvL3g4LzAP5ZfCsFHdXGHVi8OWpaE1EGZjMWya2H1YV6UCtQNLn7VHbtIPnBXbMVZs7uAC5mG7R228E37JCz6Um184Ut5iCdh76Un99nU67hdCi5tU481mU6zCJ73E822R7Gm5CAu7sZVMbXBnPItbHVhjnexHpQUVLteWCybnBnAGX6UQx8JPKmAkd1wO5eqR1UcLtRrnFFnrRtLcU1Rqe5Ow1dkAmKPJ8xQU6XGAnBnbyCWetLVUQpHxenjWRbsICupr824tpl09NhtJ0b4AEx8aVUcr4pJpJfOfZ7WFe136b44b631eFW7ZfOfJpJp4rcUVa8xEA4b0JthN90lpt428rpuCIsbRkKXu4QKJhuoPhoJQTNmGih9PkaxYFwbro4AL0eiSf7B2Mksyye88eyyskM2B7fSie0LA4orbwFYxakP9hiGmNTQJohPouhJKQ4uXK1W4S5d8hULJEQYG79PVqvARAIKDwMyrT9gI8YQ06Ya2clAV17YaaY71VAlc2aY60QY8Ig9TryMwDKIARAvqVP97GYQEJLUh8d5S4WiuzTbUPdjnNwNgD4PcMB4HKnY6f9JBWpSIQEBOF1UGPlvK944MEEM449KvlPGU1FOBEQISpWBJ9f6YnKH4BMcP4DgNwNnjdPUbTzuUOq5vPvT4yrRLyj9FFFSYQdvcb66qmoF6FGhQgtPChniv9TxA8338AxT9vinhCPtgQhGF6Fomq66bcvdQYSFFF9jyLRry4TvPv5qOseI5dZKOiYSGnWjRtoNtf1tWuEYp2WEvKKwsLFZM2EC6zKHoI0RR0IoHKz6CE2MZFLswKKvEW2pYEuWt1ftNotRjWnGSYiOKZd5IejWIIOcjXWdJTBajGjvi5ZoTUNqfFd4V1KGYiV1Gom96h7e2CK5ee5KC2e7h69moG1ViYGK1V4dFfqNUToZ5ivjGjaBTJdWXjcOIIWguD6jsIZITL0tQVSrmTrSxDu2cGKOexFwSpjwlb2g42NCsrWN7hh7NWrsCN24g2blwjpSwFxeOKGc2uDxSrTmrSVQt0LTIZIsj6Du9yvS01Bs5xoC8Qo20mTHIJulz9RC0OHtO0cfqKN5mkuWnu47bgJJgb74unWukm5NKqfc0OtHO0CR9zluJIHTm02oQ8Cox5sB10SvyLWmYFfc0oe0IKoCMC3Tcbv7UpeL9Zg5wJWVpiDOpy3BCvJNCgQQgCNJvCB3ypODipVWJw5gZ9LepU7vbcT3CMCoKI0eo0cfFYmWL'

# Python program to remove 
# all adjacent duplicates from a string

# Recursively removes adjacent 
# duplicates from str and returns
# new string. las_removed is a 
# pointer to last_removed character
def removeUtil(string, last_removed):

	# If length of string is 1 or 0
	if len(string) == 0 or len(string) == 1:
		return string

	# Remove leftmost same characters 
	# and recur for remaining 
	# string
	if string[0] == string[1]:
		last_removed = ord(string[0])
		while len(string) > 1 and string[0] == string[1]:
			string = string[1:]
		string = string[1:]

		return removeUtil(string, last_removed)

	# At this point, the first 
	# character is definiotely different
	# from its adjacent. Ignore first 
	# character and recursively 
	# remove characters from remaining string
	rem_str = removeUtil(string[1:], last_removed)

	# Check if the first character 
	# of the rem_string matches 
	# with the first character of 
	# the original string
	if len(rem_str) != 0 and rem_str[0] == string[0]:
		last_removed = ord(string[0])
		return (rem_str[1:])

	# If remaining string becomes 
	# empty and last removed character
	# is same as first character of 
	# original string. This is needed
	# for a string like "acbbcddc"
	if len(rem_str) == 0 and last_removed == ord(string[0]):
		return rem_str

	# If the two first characters of 
	# str and rem_str don't match, 
	# append first character of str 
	# before the first character of 
	# rem_str.
	return ([string[0]] + rem_str)

def remove(string):
	last_removed = 0
	return toString(removeUtil(toList(string), last_removed))

# Utility functions
def toList(string):
	x = []
	for i in string:
		x.append(i)
	return x

def toString(x):
	return ''.join(x)


print (remove(string1))


# This code is contributed by BHAVYA JAIN

