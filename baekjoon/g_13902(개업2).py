import sys

N, M = map(int,sys.stdin.readline().rsplit()) # 짜장면의 수, 웍의 개수
wok = list(map(int, sys.stdin.readline().rsplit()))

# 동시에 두 개만 가능

Max = 987654321
possible = set(wok)

# wok 으로 만들 수 있는 모든 경우의 수를 뽑아 낸다.
for i in range(M-1):
    for j in range(i+1, M):
        possible.add(wok[i]+wok[j])

possible = sorted(list(possible))
dp = [Max] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for p in possible:
        if i - p < 0:
            break
        dp[i] = min(dp[i], dp[i-p]+1)
print(dp[-1] if dp[-1] != Max else -1)





