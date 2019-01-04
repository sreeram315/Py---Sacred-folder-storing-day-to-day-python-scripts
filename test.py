# proprietary to BEERA // DO NOT COPY
if __name__ == '__main__':
    groups    =   int(input())
    stud    =   []
    cost = 0
    i = 0
    s4,s2,s3,s1 = 0,0,0,0
    for _ in range(groups):
        a = int(input())
        if a==4: s4+=1
        elif a==3: s3+=1
        elif a==2: s2 +=1
        elif a==1: s1 += 1
    cost += s4*500
    print(f'cost after 4\'s is {cost}')
    m31 =   min(s3,s1)
    cost    += m31*500
    print(f'cost after 3,1\'s is {cost}')
    s3-=m31
    s1-=m31
    while s1/2 > s2:
        cost += 500
        s1-=2
        s2-=1
    print(f'cost after 2,1\'s is {cost}')
    print(s1,s2,s3,s4)
    cost    += (s1 +s2+s3)*500
    print(cost)
        
            
    
        
    
        