import math
import itertools, functools, operator

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

def rule_asc(n):
    total = 0
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        total += 1
        # yield a[:k + 1]
    return total

def composition(n):
    return 2 ** (n - 1)

def partition(n, r): # sum n from numbers no more than r
    if n == r:
        return 1 + partition(n, r - 1)
    if r == 0 or n < 0:
        return 0
    if n == 0 or r == 1:
        return 1

    return partition(n, r - 1) + partition(n - r, r)
    # source: https://stackoverflow.com/questions/14053885/integer-partition-algorithm-and-recursion

def partition_non_empty(n, r):
    total = 0
    if n < r:
        return 0
    if n == r or n == r + 1 or r == 1:
        return 1
    if r == 2:
        return n // 2

    if n <= 2 * r:
        return rule_asc(n - r)

    for i in range(1, r + 1):
        total += partition_non_empty(n - r, i)

    return total
    # source: https://brilliant.org/wiki/identical-objects-into-identical-bins/

print rule_asc(3)
