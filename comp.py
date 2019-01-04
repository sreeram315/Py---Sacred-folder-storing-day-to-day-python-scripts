# proprietary to BEERA // DO NOT COPY
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst
lst=[]
[lst.append(i*j) for i in range(10) for j in range(10)]

print(lst)