
def ccon():
    n = 1
    while True:
        for c in str(n):
            yield c
        n += 1

def cycle(targets=[1,10,100,1000,10000,100000,1000000]):
    n = 1
    c = ccon()
    while targets:
        temp = c.next()
        if n in targets:
            yield temp
            targets.pop(0)
        n += 1



