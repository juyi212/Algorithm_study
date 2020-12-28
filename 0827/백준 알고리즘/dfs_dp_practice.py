import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dp(x):
    if x ==1:
        return 1
    if x == 2:
        return 2
    if dx[x]:
        return dx[x]
    else:
        dx[x] = dp(x - 1) + dp(x - 2)
    return dx[x]

n=int(input())
dx=[0]*(n+1)
print(dp(n)%10007)