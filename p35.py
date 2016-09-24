from utils import prime

def rotations(s):
    orig = str(s)
    s = list(s)
    while True:
        t = s.pop(0)
        s.append(t)
        yield ''.join(s)
        if ''.join(s) == orig:
            break

def answer(limit):
    return [x for x in xrange(2,limit) if prime(x) and all([prime(int(y)) for y in rotations(str(x))])]
