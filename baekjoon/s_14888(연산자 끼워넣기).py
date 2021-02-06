# import sys
#
# def cal(p1, p2, i):
#     # 숫자 두개와 연산자 하나가 들어와야 함.
#     if i == 0:
#         return p1 + p2
#     elif i == 1:
#         return p1 - p2
#     elif i == 2:
#         return p1 * p2
#     elif i == 3:
#         # 연산 주의
#         if p1 < 0:
#             ans = abs(p1)//p2
#             return -ans
#         return p1//p2
#
#
# def check(n1, idx):
#     global max_v, min_v
#
#     if idx >= len(numbers):
#         if n1 > max_v:
#             max_v = n1
#         if n1 < min_v:
#             min_v = n1
#
#     for i in range(len(operators)):
#         if operators[i]:
#             operators[i] -= 1
#             a = cal(n1, numbers[idx], i)
#             check(a, idx+1)
#             operators[i] += 1
#
#
# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
#
# # +, -, x, //
# operators = list(map(int, sys.stdin.readline().split()))
# # oper idx, number idx, 계산된 값.
# max_v, min_v = -1000000000, 1000000000
# check(numbers[0], 1)
# print(max_v)
# print(min_v)

# 수의 순서는 정해져있고
# operators 의 순서가 바껴야함
# 하나씩 끼워지면서 계산.
# operators의 idx를 더하고 빼면서 계산하기
# 연산을 할 때 조심해야함

import sys

# 시간 줄이는 방법
def dfs(index, result, add, sub, mul, div):
    global max_v, min_v

    if index == n:
        if max_v < result:
            max_v = result
        if min_v > result:
            min_v = result
    else:
        if add:
            dfs(index+1, result+numbers[index], add-1, sub, mul, div)
        if sub:
            dfs(index+1, result-numbers[index], add, sub-1, mul, div)
        if mul:
            dfs(index + 1, result * numbers[index], add, sub, mul-1, div)
        if div:
            dfs(index + 1, int(result / numbers[index]), add, sub, mul, div-1)


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
a, b, c, d = map(int, sys.stdin.readline().split())
max_v = -1e9
min_v = 1e9
dfs(1, numbers[0], a, b, c, d)
print(max_v)
print(min_v)