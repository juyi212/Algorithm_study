import sys


def check(trees, mid):
    remain = 0
    for t in trees:
        if t > mid:
            remain += (t-mid)
    return remain


n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

l, r = 0, max(trees)
max_v = -1

while l <= r:
    mid = (l+r)//2
    remain = check(trees, mid)

    if remain >= m:
        max_v = mid
        l = mid+1
    else:
        r = mid-1
print(max_v)