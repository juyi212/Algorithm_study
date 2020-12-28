import sys

# dp로 풀어야함
# def check(idx, p):
#     global ans
#     if idx > N:
#         return
#     if idx == N:
#         ans = max(ans, p)
#         return
#     check(idx+1, p)
#     check(idx + time[idx], p+pay[idx])

# def check(idx, cost):   #backtracking
#     global max_p
#     if idx + time[idx] == N+1:
#         if cost + pay[idx] > max_p:
#             max_p = cost + pay[idx]
#     elif idx+time[idx] > N+1:
#         if cost > max_p:
#             max_p = cost
#     else:
#         for n in range(idx+time[idx], N+1):
#             check(n, cost+pay[idx])


def check(idx, cost):
    global max_p
    if idx + time[idx] == N+1:
        if cost + pay[idx] > max_p:
            max_p = cost + pay[idx]

    elif idx + time[idx] > N+1:
        if cost > max_p:
            max_p = cost
    else:
        for n in range(idx + time[idx], N+1):
            check(n, cost + pay[idx])


N = int(input())
time = [1]
pay = [0]
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    time.append(t)
    pay.append(p)
max_p = 0
check(0, 0)
print(max_p)



# dp = [0 for _ in range(N+1)]
#
# for i in range(len(time)-1, -1, -1):
#     if time[i] + i <= N:
#         dp[i] = max(pay[i]+dp[i+time[i]], dp[i+1])
#     else:
#         dp[i] = dp[i+1]
# print(dp)
# print(dp[0])



# check(0, 0)
# print(ans)