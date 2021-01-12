# from collections import Counter
#
# def solution(a):
#     n = len(a)
#     if n <= 1:
#         return 0
#     counter = [0] * n+1
#     limit = [-1] * n+1
#     for idx, k in enumerate(a):



def solution(a):
    ans = 0
    dic = {}
    check = {}
    for i in range(len(a)):
        dic[i] = 0
        check[i] = -2

    for i in range(len(a) - 1):
        if a[i] != a[i+1]:
            if check[a[i]] != i-1:
                dic[a[i]] += 1
                check[a[i]] = i
            if check[a[i+1]] != i-1:
                dic[a[i+1]] += 1
                check[a[i+1]] = i

    return max(dic.values()) * 2


# 승한
# def solution(a):
#     answer = -1
#     N = len(a)
#
#     if N <= 1:
#         return 0
#
#     counter = [0] * (N + 1)
#     limit = [-1] * (N + 1)
#     for idx, k in enumerate(a):
#         if limit[k] >= idx:
#             continue
#
#         if limit[k] < idx - 1:
#             # 왼
#             limit[k] = idx
#             counter[k] += 1
#         elif limit[k] == idx - 1 and idx + 1 < len(a):
#             if a[idx + 1] != k:
#                 # 오른쪽 묶임
#                 limit[k] = idx + 1
#                 counter[k] += 1
#             else:
#                 # 왼 오 다 안되는 경우
#                 limit[k] = idx
#
#     answer = max(counter) * 2
#     return answer


a = [0,3,3,0,7,2,0,2,2,0]
print(solution(a))