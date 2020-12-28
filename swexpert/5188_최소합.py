
def dfs(x, y, total):  # 현재위치 행, 열
    global min_p
    if x == N-1 and y == N-1:
        if total < min_p:
            min_p = total
    else:
        if x+1 < N and min_p > total + matrix[x+1][y]:
            dfs(x+1, y, total + matrix[x+1][y])
        if y + 1 < N and min_p > total + matrix[x][y+1]:
            dfs(x, y+1, total + matrix[x][y+1])


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_p = 10000000
    dfs(0, 0, matrix[0][0])
    print('#{} {}'.format(tc,min_p))    # 열과 행 둘중 하나만 중가하는 경우

