
a = list(map(int, input().rstrip()))

# cnt[i] = cnt[i-1] + cnt[i-2] 점화식
l = len(a)
dp = [0] * (l + 1)

if a[0] == 0:
    print(0)
else:
    a = [0] + a
    dp[0] = 1
    dp[1] = 1 # 첫번째 수로 이뤄진 암호코드는 1이다

    for i in range(2, l+1):
        cur = a[i]
        tcur = a[i-1] * 10 + a[i]   # 두 자리 수
        if 1 <= cur < 10:
            dp[i] += dp[i-1]
        if tcur >= 10 and tcur <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000
    print(dp[l])







    

# dp 문제
# 하나씩 빼고 다음은 맨 처음이 두개 하나하나..
# 1보다 크고 27보다 작은 숫자들

