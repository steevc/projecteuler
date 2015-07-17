__author__ = 'steve'
sumsq = sum(x**2 for x in range(1,101))
sqsum = (sum(x for x in range(1,101)))**2
print('%s - %s = %s' % (sqsum, sumsq, sqsum - sumsq))