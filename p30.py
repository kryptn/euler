

def n_power_sum(n, power):
    return sum([int(x)**power for x in str(n)])

def answer(limit):
    return sum([x for x in xrange(2,limit) if x == n_power_sum(x, 5)])
