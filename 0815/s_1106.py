def dpdp(N, C, dp):
    for i in range(N):
        for j in range(1, C+1):
            dp[0] = 0
            h = j - hotels[i][1]
            if h <= 0: # 위의 식이 음수가 나올경우는 다 index 0에 0값으로 다 넣어줌.
                h = 0
            if dp[j] == -1: #아닐경우는 첫 도시에
                dp[j] = dp[h] + hotels[i][0] # cost를 쌓아가는 형식 / 첫 도시의 경우 3,6,9
            else: # 두번째 도시 들어오면서 값 비교
                dp[j] = min(dp[j], dp[h] + hotels[i][0]) # 적어도
    return dp


C, N = map(int, input().split())
hotels = [list(map(int, input().split())) for _ in range(N)]
dp = [-1]*(C+1) # 값을 저장해줄 빈 공간
print(dpdp(N, C, dp)[C])