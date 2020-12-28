def check(dp, a):
    s, e = 0, len(dp)-1

    while s < e:
        m = (s+e)//2
        if dp[m] < a:
            e = m
        else:   # dp[m] > a?
            s = m+1
    return e    # 젤 큰값과 변경


n = int(input())
matrix = list(map(int, input().split()))

dp = []

for i in matrix:
    if not dp or dp[-1] > i:
        dp.append(i)
    else:   # dp[-1] < i 큰 값을 교체해줄 자리를 찾는다
        dp[check(dp, i)] = i

print(dp)
print(len(dp))


'''
6
10 30 10 20 20 10


5
7 5 3 1 10
'''

# easy method
# def sol(n, matrix):
#
#     li = [matrix[0]]
#     idx = 0
#     for i in range(1, n):
#         if li[idx] > matrix[i]:
#             li.append(matrix[i])
#             idx += 1
#         else: # li[idx] <= matrix[i]
#             for j in range(idx+1):
#                 if li[j] <= matrix[i]:
#                     li[j] = matrix[i]
#                     break
#     idx += 1
#     print(li)
#     return idx
#
#
#
# n = int(input())
# matrix = list(map(int, input().split()))
#
# print(sol(n, matrix))