import sys
from bisect import bisect_left


# def lis(arr):
#     if not arr:
#         return 0
#
#     # C[i] means smallest last number of lis subsequences whose length are i
#     INF = float('inf')
#     C = [INF] * (len(arr)+1)
#     C[0] = -INF
#     C[1] = arr[0]
#     tmp_longest = 1
#
#     # Find i that matches C[i-1] < n <= C[i]
#     def search(lo, hi, n):
#         if lo == hi:
#             return lo
#         elif lo + 1 == hi:
#             return lo if C[lo] >= n else hi
#
#         mid = (lo + hi) // 2
#         if C[mid] == n:
#             return mid
#         elif C[mid] < n:
#             return search(mid+1, hi, n)
#         else:
#             return search(lo, mid, n)
#
#
#     for n in arr:
#         if C[tmp_longest] < n:
#             tmp_longest += 1
#             C[tmp_longest] = n
#         else:
#             next_loc = search(0, tmp_longest, n)
#             C[next_loc] = n
#     print(C)
#     return tmp_longest


def check(li, a):
    s, e = 0, len(li)-1

    while s <= e:
        m = (s+e)//2
        if li[m] > a:
            e = m-1
        else:
            s = m + 1
    return s


n = int(input())
arr = list(map(int, input().split()))
link = []

for a in arr:
    if not link or link[-1] < a:
        link.append(a)
    else:
        link[check(link, a)] = a    # a값이 있는 사이에 가장 큰 값중   작은 값의 인덱스를 찾아서 넣어준다.
print(len(arr) - len(link))



