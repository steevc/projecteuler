__author__ = 'steve'
from math import sqrt
p=[2, 3]

def isprime(n):
    ip = True
    for x in p:
        if n % x == 0:
            ip = False
            break
    return ip

c=2
n = 3
while c < 10001:
    n += 2
    #print(n)
    if isprime(n):
        c += 1
        p.append(n)
        print('%s %s' % (c, n))

