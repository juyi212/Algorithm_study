def dp(x):
    if x ==1:
        return 1
    elif x == 2:
        return 3
    return dp(x-1)+(2*dp(x-2))

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    c=dp(n//10)
    print(f'#{tc} {c}')