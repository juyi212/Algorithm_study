# 조합
# def check(idx):
#
#     ch = res.count(1)
#     if ch == m:
#         re = []
#         for i in range(len(res)):
#             if res[i] == 1:
#                 re.append(i)
#         result.append(re)
#         return
#     if idx == n:
#         return
#
#
#
#     res[idx] = 1
#     check(idx+1)
#     res[idx] = 0
#     check(idx+1)

#
# n, m = map(int, input().split())
# result = []
# res =[0] * n
# check(0)
# print(result)

# 순열
from itertools import permutations

n, m = map(int, input().split())
a = permutations(list(range(1, n+1)), m)

for i in a:
    print(*i)

