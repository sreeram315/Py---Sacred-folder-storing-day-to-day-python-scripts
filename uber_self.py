# proprietary to BEERA // DO NOT COPY



def fact(a):
	if a == 0 or a == 1:
		return 1
	return int(a*fact(a-1))

def process(n, a):
	return int(fact(n)/fact(n-a))

if __name__ == '__main__':
	n 	=  int(input())
	arr	=	[0 for _ in range(n+1)]
	for i in range(1, n+1):
		arr[i]		=	process(n, i) + arr[i-1]

	print(arr[n])