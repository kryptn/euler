
def palendrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

def answer(limit):
    return sum([x for x in xrange(limit+1) if palendrome(x) and palendrome(bin(x)[2:])])

