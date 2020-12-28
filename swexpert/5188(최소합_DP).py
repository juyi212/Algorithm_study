# 위쪽과 위쪽의 최소값 + 햔재위치 값
# D[r][c] =  min(D[r-1][c], D[r][c-1])

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 각 칸에 도착하기 위해서 드는 최소 비용을 저장하는 배열
    memo = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                memo[i][j] = matrix[i][j]
                continue
            if i == 0:
                memo[i][j] = memo[i][j-1] + matrix[i][j]
                continue
            if j == 0:
                memo[i][j] = memo[i-1][j] + matrix[i][j]
                continue
            memo[i][j] = min(memo[i-1][j], memo[i][j-1]) + matrix[i][j]
    print(memo[N-1][N-1])
