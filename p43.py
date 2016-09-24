from itertools import permutations

tests = [2,3,5,7,11,13,17]

def pantest(s):
    tests = [2,3,5,7,11,13,17]
    for i, v in enumerate(tests):
        if int(s[i+1:i+4]) % v:
            return False
    return True

def main():
    return sum((int(''.join(x)) for x in permutations('0123456789') if pantest(''.join(x))))

