from functools import wraps
from multiprocessing import Pool
from time import time
from fractions import gcd
import math

def factorial(n):
    return reduce(lambda x,y:x*y,xrange(2,n+1))


def factors(n):
    return set(reduce(list.__add__,
                      ([x, n/x] for x in xrange(1, int(math.sqrt(n)+1)) if n % x == 0)))

def prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % x for x in xrange(3, int(math.sqrt(n)) + 1, 2))

def prime_factors(n, limit=None):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if limit and d > limit:
            return [limit+1]
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def coprime(x,y):
    if gcd(x,y) == 1:
        return True
    return False

def euler_totient(n):
    return sum((coprime(x,n) for x in xrange(n)))
