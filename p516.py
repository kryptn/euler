import utils

def gcd(x,y):
    while y != 0:
        (x, y) = (y, x%y)
    return x

def hamming(n,limit=None):
    phi = utils.euler_totient(n)
    pf = utils.prime_factors(phi, limit)
    if max(pf) <= 5:
        return True
    return False

def ham(n, limit=None):
    return n if hamming(n, limit) else 0

def S(L):
    return sum(x for x in xrange(3, L+1) if hamming(x))

