__author__ = 'steve'
from math import sqrt
p=[2, 3]

def isprime(n):
    ip = True
    s = sqrt(n)+1
    for x in p:
        if x > s:
            break
        if n % x == 0:
            ip = False
            break
    return ip

c = 2
n = 3
while n < 1999999:
    n += 2
    #print(n)
    if isprime(n):
        c += 1
        p.append(n)
print(sum(p))
