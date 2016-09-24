from decimal import *

def getset(n):
    getcontext().prec = 1000
    return {x:str(Decimal(1)/Decimal(x)) for x in xrange(1,n+1)}

def cyclic(p):
    b = 10
    t = 0
    r = 1
    n = 0
    while True:
        t += 1
        x = r*b
        d = int(x/p)
        r = x % p
        n = n*b+d
        if r == 1:
            break

    if t == p-1:
        return True
    
    return False
