def bin(x):
    arr = []
    while(x):
        arr.append(x%2)
        x = int(x/2) 
    return arr
from copy import deepcopy
def me(A, B):
	m = max(len(A), len(B))
	if(len(A) < m):
		while(len(A) != m):
			A.append(0)
	if(len(B) < m):
		while(len(A) != m):
			B.append(0)
	return A, B

def dec(X):
	i = 0
	num = 0
	for x in X:
		num += x*(2**i)
		i += 1
	return num

def ch(X, i, k, lo, hi, B):
	X[i] = not X[i]
	print("*",  dec(X), dec([X[i]^A[i] for i in range(len(A))]))
	print(dec([X[i]^B[i] for i in range(len(B))]) <= k and (dec(X) >= lo) and (dec(B) <= hi))
	return dec([X[i]^B[i] for i in range(len(B))]) <= k and (dec(X) >= lo) and (dec(B) <= hi)

def ch2(X, i, k, lo, hi, A):
	X[i] = not X[i]
	print(".", dec(X), dec(A), dec([X[i]^A[i] for i in range(len(A))]))
	print(dec([X[i]^A[i] for i in range(len(A))]) <= k and (dec(A) >= lo) and (dec(X) <= hi))
	return dec([X[i]^A[i] for i in range(len(A))]) <= k and (dec(A) >= lo) and (dec(X) <= hi)


def maxXor(lo, hi, k):
	# print(bin(lo), (bin(hi)))
	A, B = me(bin(lo), bin(hi))
	print((A), (B))
	# return 0
	C = []
	for i in range(len(A)):
		if(A[i] == B[i]):
			if(not A[i]) and ch(deepcopy(A), i, k, lo, hi, B):
				A[i] = 1
			elif(B[i] and ch2(deepcopy(B), i, k, lo, hi, A) ):
				B[i] = 0
		C.append(A[i]^B[i])
	print(dec(A), dec(B))
	print(C)
	return dec(C)


print(maxXor(11, 61, 32))





