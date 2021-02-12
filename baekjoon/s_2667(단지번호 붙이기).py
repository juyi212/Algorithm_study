import sys
from collections import deque


def bfs(r, c, visited):
    visited[r][c] = True
    q = deque()
    q.append([r, c])
    cnt = 1

    while q:
        r, c = q.popleft()
        for dr, dc in ([(-1, 0), (1, 0), (0, -1), (0, 1)]):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                cnt += 1
                q.append([nr, nc])

    return cnt


n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j, visited))

result.sort()
print(len(result))
for i in result:
    print(i)
