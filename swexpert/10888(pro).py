t = int(input())


def solve(k):
    global ans
    if k == len(food):
        tsum = 0
        for h in range(len(home)):
            tmin = 1e9
            for f in range(len(subset)):
                if subset[f]:
                    tmin = min(tmin, dist[f][h])
            tsum +=  tmin
        for f in range(len(subset)):
            if subset[f]:
                tsum += food[f][2]
        if ans > tsum:
            ans = tsum
    else:
        subset[k] = 1
        solve(k + 1)
        subset[k] = 0
        solve(k + 1)


for tc in range(1, t+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    home, food =[], []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:    #집
                home.append((i, j))
            elif matrix[i][j] > 1:   #배달
                food.append((i, j, matrix[i][j]))

    dist = [[0] * len(home) for _ in range(len(food))]
    for i in range(len(food)):
        for j in range(len(home)):
            dist[i][j] = abs(food[i][0] - home[j][0]) + abs(food[i][1] - home[j][1])    #배달지 기준 각각의 집과의 거리
    print(dist)
    ans = 1e9
    subset = [0] * len(food)
    solve(0)
    print(f'#{tc} {ans}')