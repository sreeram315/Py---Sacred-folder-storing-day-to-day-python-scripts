#!/bin/python3

import os
import sys
import heapq
from heapq import heapify, heappop, heappush

def cookies(k, A):
    heapq.heapify(A) 
    ops = 0
    while not ( A[0] >= k ):
        if len(A) == 1:
            return -1
        ops += 1
        l1, l2 = heapq.heappop(A), heapq.heappop(A)
        new_el = l1 + 2*l2
        heapq.heappush(A, new_el) 
    return ops
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
