# proprietary to BEERA // DO NOT COPY


if __name__ == '__main__':
	n 			=		int(input())
	if n == 1:
		print('0')
		exit()
	arr			=		list(map(int, input().split()))
	arr.sort()
	#print('arr =',arr )
	answer		=		[None for _ in range(n-1)]
	answer[0]	=		arr[0] + arr[1]
	for i in range(1, n-1):
		answer[i]	=	answer[i-1] + arr[i+1]
	for i in answer: print(i, end=' ')
