from math import sqrt
from functools import reduce


def appendEs2Sequences(sequences, es):
    result = []
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result += [seq + [e] for seq in sequences]
    return result


def primefactors(n):
    '''
    Takes a number and returns all of it's prime factors
    '''
    print('asking for',n)
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            l = primefactors(n // i)
            l.append(i)
            return l
        i += 1 
    return [n]      # if number is less than or equala to 4, returns [n]


def factorGenerator(n):
    p = primefactors(n)
    factors = {}
    for p1 in p:
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors


def divisors(n):
    factors = factorGenerator(n)
    divisors = []
    print(f'factors = {factors}')
    listexponents = [list(map(  lambda x:k ** x, list(range(0, factors[k] + 1))   )) for k in factors.keys()]
    print('lsls',listexponents)
    listfactors = reduce(appendEs2Sequences, listexponents, [])
    print(listfactors)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x * y, f, 1))
    divisors.sort()
    return divisors


print(divisors(1000))



