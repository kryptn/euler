from utils import factors
from multiprocessing import Pool

def abundant(n):
    f = sorted(list(factors(n)))[:-1]
    if sum(f) > n:
        return True
    return False

def getabundants(n):
    return [x for x in xrange(1,n+1) if abundant(x)]

ab = getabundants(28123)

def asum(n):
    for x in filter(lambda x: x<n/2+1, ab):
        if n-x in ab:
            return 0

    return n

def answer():
    ab = getabundants(28123)
    p = Pool(8)
    r = sum(p.map(asum, xrange(1,28124)))
    return r
