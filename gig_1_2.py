# proprietary to BEERA // DO NOT COPY


if __name__ == '__main__':
	n 			, cost, ultimate_sum	=	 int(input()), [], 0
	for _ in range(n): cost.append(int(input()))
	multipliers		=	[0 for _ in range(n)]
	multipliers[0]	=	cost[0]
	for i in range(1, n):
		multipliers[i]	=	(cost[i]*(i+1)) + multipliers[i-1]
	for i in range(n):
		ultimate_sum 	+=	multipliers[i]*cost[i]
	print(ultimate_sum % modulo)

