# proprietary to BEERA // DO NOT COPY
#python3
stck_size = 0
time = 0
size, n = list(map(int, input().split()))
if n == 0: exit()
#print('size==',size,'n==',n)
arrival =[0] * n
ptime = [0] * n
ans = [0] * n
for i in range(n):
	#print('i==',i)
	arrival[i], ptime[i] = list(map(int, input().split()))
	#print('arrival[i]==',arrival[i],'ptime[i]==',ptime[i])
for i in range(len(arrival)):
	#print('i==',i)
	a = arrival.pop(0)
	p = ptime.pop(0)
	if a < time:
		ans[i] = -1
		continue
	stck_size += 1
	if stck_size > size:
		ans[i] = -1
	else:
		ans[i] = a
		time += p
		stck_size -= 1

for i in ans: print(i)


