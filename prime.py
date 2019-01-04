# proprietary to BEERA // DO NOT COPY
def is_prime(a):
    return all(a % i for i in range(2, a))

for i in range(9999999, 99999999999):
	if is_prime(i):
		print(i)