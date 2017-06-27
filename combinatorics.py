# def partition(n):
    # source: https://brilliant.org/wiki/partition-of-an-integer/#conjugate-partitions

import math
import itertools, functools, operator

def maxWidth(n):
    return int((-1 + math.sqrt(1 + 8 * n)) // 2)

def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def answer(n):
    ans = 0
    for k in range(2, int((-1 + math.sqrt(1 + 8 * n)) // 2) + 1):
        ans += len(list(itertools.ifilter(lambda x: sum(x) == n and not 0 in x ,itertools.combinations(range(n), k))))
    return ans

n = 10
k = 3
print itertools.ifilter(lambda x: sum(x) == n and not 0 in x ,itertools.combinations(range(n), k)), 1)
    # your code here
