
def solve(k):
    global total
    if k == len(franchise):
        tsum = 0
        for h in range(len(dist[1])):
            tmin = 10000000
            for f in range(len(subset)):
                if subset[f]:
                    tmin = min(tmin, dist[f][h])
            tsum += tmin
        for f in range(len(subset)):
            if subset[f]:
                tsum += franchise[f][2]

        if total > tsum:
            total = tsum

    else:
        subset[k] = 1
        solve(k + 1)
        subset[k] = 0
        solve(k + 1)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    franchise = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 1:
                franchise.append((i, j, matrix[i][j]))

    # 음식배달집 모든경우 다 봐야함. 조합론 (부분집합)
    dist = [[] for _ in range(len(franchise))]
    for r in range(n):
        for c in range(n):
            min_d = n*n
            if matrix[r][c] == 1:
                for k in range(len(franchise)):
                    c2, r2 = franchise[k][0], franchise[k][1]
                    dist[k].append(abs(r-r2) + abs(c-c2))

total = 1000000000
subset = [0] * len(franchise)
solve(0)
print(total)

'''
1
9
0 0 0 0 0 0 0 0 0
0 5 0 0 5 0 0 5 0
0 0 1 0 1 0 1 0 0
0 0 0 0 0 0 0 0 0
0 5 1 0 30 0 1 5 0
0 0 0 0 0 0 0 0 0
0 0 1 0 1 0 1 0 0
0 5 0 0 5 0 0 5 0
0 0 0 0 0 0 0 0 0
'''