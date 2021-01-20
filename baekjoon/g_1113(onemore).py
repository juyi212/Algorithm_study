import sys
import collections


def start(h):
    res = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and 0 < pool[i][j] < h:
                res += bfs(i, j, h)
    return res


def bfs(i, j, h):
    visited[i][j] = True
    q = collections.deque()
    q.append((i, j))
    pos = [(i, j)]
    flag = False
    while q:
        i, j = q.popleft()
        for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            nx, ny = i+dx, j+dy
            if 0 <= nx < n and 0 <= ny < m and pool[nx][ny] != 0:
                if not visited[nx][ny] and pool[nx][ny] < h:
                    q.append((nx, ny))
                    pos.append((nx, ny))
                    visited[nx][ny] = True
            else:
                flag = True
    if flag:
        return 0
    else:
        water = 0
        for i, j in pos:
            pool[i][j] += 1
            water += 1
        return water


n, m = map(int, sys.stdin.readline().split())
pool = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
total = 0
for h in range(1, 10):
    visited = [[False]*m for _ in range(n)]
    total += start(h)
print(total)