import sys
import bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
link = []

for a in arr:
    if not link or link[-1] < a:
        link.append(a)
    else:
        # 경우에는 a 가 들어갈 자리를 찾아야 함
        # 같은 숫자의 경우는 제외해준다.
        idx = bisect.bisect_left(link, a)
        link[idx] = a

print(len(link))
# def check(link, a):
#     s, e = 0, len(link)-1
#
#     while s <= e:
#         m = (s+e)//2
#         if link[m] > a:
#             e = m - 1
#         else:
#             s = m + 1
#     return s
#
#
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# link = []
#
# for a in arr:
#     if not link or link[-1] < a:
#         link.append(a)
#     elif link[-1] > a and a not in link:
#         # 경우에는 a 가 들어갈 자리를 찾아야 함
#         # 같은 숫자의 경우는 제외해준다.
#         link[check(link, a)] = a
#
# print(len(link))

'''
10 
1 5 10 3 13 18 19 15 16 17 

'''

'''
5
1 1 2 1 1

'''

