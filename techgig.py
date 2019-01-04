# proprietary to BEERA // DO NOT COPY



size = 3
cost = [1,2,3]
summ = 0
ultra_sum = 0
new_array = []


# for each_item in range(size):
# 	for last in range(size):
# 		for i in range(each_item, last+1):
# 			summ += cost[i]
# 		ultra_sum += summ*cost[last]
# 		summ = 0

for i in range(size):
	new_array.append(sum(cost[:i+1]))
print(new_array)

for i in range(size):
	ultra_sum += cost[i]*new_array[i]



print(ultra_sum%((10**9)+7))
