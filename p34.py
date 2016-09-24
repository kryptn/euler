from math import factorial

def answer(limit):
    return sum([x for x in xrange(3, limit+1) if x == sum([factorial(int(y)) for y in str(x)])])
