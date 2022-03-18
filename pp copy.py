



def get(N, R):
	M = 1000000007
	if(R > N): return 0;
	if(R == N): return 1;
	prev = 1; n = R;
	while(n < N):
		n += 1;
		prev = ((n*prev)/(n-R));
		print(f'{n}C{R} = {prev%M}');
get(84, 56)


