#FYI IT DOESNT WORK

import math

def maxWidth(n):
    return int((-1 + math.sqrt(1 + 8 * n)) // 2)

def remainingBricks(width, n):
    return n - width * (width + 1) * .5

def partition(n, r): # sum n from numbers no more than r
    if n == r:
        return 1 + partition(n, r - 1)
    if r == 0 or n < 0:
        return 0

    if n == 0 or r == 1:
        return 1

    return partition(n, r - 1) + partition(n - r, r)
    # source: https://stackoverflow.com/questions/14053885/integer-partition-algorithm-and-recursion

    # total = 0
    # a = [0 for i in range(n + 1)]
    # k = 1
    # a[1] = n
    # while k != 0:
    #     x = a[k - 1] + 1
    #     y = a[k] - 1
    #     k -= 1
    #     while x <= y:
    #         a[k] = x
    #         y -= x
    #         k += 1
    #     a[k] = x + y
    #     total += 1
    # return total
    # # source: http://jeromekelleher.net/tag/integer-partitions.html

def answer(n):
    ans = 0
    for k in range(2, maxWidth(n) + 1):
        ans += partition(remainingBricks(k, n), k)
        # print "width: " + str(k) + " remainingBricks: " + str(remainingBricks(k, n)) + " ways: " + str(partition(remainingBricks(k, n), k))
    return ans

n = 200
k = 3
print answer(n)
