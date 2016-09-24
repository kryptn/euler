from utils import prime

def formula_test(a,b):
    n = 0
    while True:
        if prime(n**2 + a*n + b):
            n += 1
        else:
            break
    return n

def answer():
    r = {}
    for x in xrange(-1000,1001):
        for y in xrange(-1000,1001):
            z = formula_test(x,y)
            if z not in r.keys():
                r[z] = []
            r[z].append((x,y))

    return r                    
