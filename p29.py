

def answer(limit):
    r = []
    for x in xrange(2, limit+1):
        for y in xrange(2, limit+1):
            r.append(x**y)

    return set(r)
