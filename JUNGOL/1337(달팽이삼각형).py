n = int(input())

dir = [(1, 1), (0, -1), (-1, 0)]
matrix = [[-1]*n for _ in range(n)]

num = 0
visited = [[False]*n for _ in range(n)]
nr, nc = 0, 0
matrix[nr][nc] = 0
visited[nr][nc] = True
cnt = 0

while cnt <= (n*n):
    for r, c in dir:
        while True:
            cnt += 1
            nr += r
            nc += c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if num < 9:
                    num += 1
                    visited[nr][nc] = True
                    matrix[nr][nc] = num
                else:
                    num = 0
                    visited[nr][nc] = True
                    matrix[nr][nc] = num
            else:
                nr -= r
                nc -= c
                break

for i in matrix:
    for j in i:
        if j != -1:
            print(j, end = ' ')
    print()


