__author__ = 'steve'
found=False
for a in range(1, 998):
    for b in range(a, 998):
        c=1000-a-b
        if c < 1:
            break
        if c**2==a**2+b**2:
            found=True
            break
    if found:
        break
print('%s %s %s' % (a,b,c))
print('%s %s %s' % (a**2,b**2,c**2))
print(a*b*c)
