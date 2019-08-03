





T = int(input())
for _ in range(T):
    
    dic = {}
    N = int(input())
    mems = list(map(int, input().split()))
    print(f'Case #{_ + 1}:', end=' ')
    
    for i in range(len(mems)):
        dic[str(chr(i + 1 + 64))] = mems[i]

    print(dic)
    
    dic = dict(sorted(dic.items(), key = lambda kv: kv[1], reverse = True))
    

    while(next(iter(dic.values())) != 0):
    	print('\n\n')
    	print(dic)
    	print('\n\n')


    	var = []
    	count = 0
    	for key, value in dic.items():
    		if value != 0:
    			var.append(key)
    		count += 1
    		if count==2: break

    	

    	for v in var:
    		dic[v] -= 1
    		print(v, end = '')
    	print(' ', end = '')

    	dic = dict(sorted(dic.items(), key = lambda kv: kv[1], reverse = True))

    if _+1 < T: print('\n', end='')
    
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
