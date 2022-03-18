# Python 3 program to find modular 
# inverse of a under modulo m 

# A naive method to find modulor 
# multiplicative inverse of 'a' 
# under modulo 'm' 
def modInverse(a, m) : 
	a = a % m; 
	for x in range(1, m) : 
		if ((a * x) % m == 1) : 
			return x 
	return 1

# Driver Program 
a = 35
m = 3
print(modInverse(a, m)) 

#This code is contributed by Nikita Tiwari. 
