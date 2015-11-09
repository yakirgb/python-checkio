from math import factorial
from operator import mul
from functools import reduce

def fac1(n):
    if n == 0:
        return 1
    else:
        return n * fac1(n-1)

def fac2(n):
    return 1 if n==0 else n * fac2(n-1)


def fac3(n):
    return factorial(n)


fac4 = lambda n: 1 if n == 0 else n * fac4(n-1)


fac5 = lambda n: reduce(mul, range(n, 0, -1))

print(fac1(5))
print(fac2(5))
print(fac3(5))
print(fac4(5))
print(fac5(5))