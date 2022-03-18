
from time import sleep

arr = [1, 0, 0, 0]
i = 4; count = 1
print(arr[i-4],arr[i-3],arr[i-2],arr[i-1])
while(True):
	arr.append((arr[i-4]+arr[i-1])%2); i += 1;
	arr.append((arr[i-4]+arr[i-1])%2); i += 1;
	arr.append((arr[i-4]+arr[i-1])%2); i += 1;
	arr.append((arr[i-4]+arr[i-1])%2); i += 1;
	count += 1
	print(arr[i-4],arr[i-3],arr[i-2],arr[i-1], ' - ', count)
	sleep(0.1)

