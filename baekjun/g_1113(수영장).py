import sys
import collections


def bfs(i, j, h):
    q = collections.deque()
    q.append([i, j])
    visited[i][j] = True
    hi = [[i, j]]
    v = False
    while q:
        i, j = q.popleft()
        for x, y in ([-1, 0], [1, 0], [0, 1], [0, -1]):
            nx, ny = i+x, j+y
            if 0 <= nx < n and 0 <= ny < m and swimming[nx][ny] != 0:
                if not visited[nx][ny] and swimming[nx][ny] < h:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    hi.append([nx, ny])
            else:   #가장자리에 있는 것들
                v = True

    if v:
        return 0
    else:
        water = 0
        for i in range(len(hi)):
            x, y = hi[i][0], hi[i][1]
            swimming[x][y] += 1
            water += 1
        return water


n, m = map(int, sys.stdin.readline().split())
swimming = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
result = 0
for k in range(1, 10):  # 높이를 기준으로
    visited = [[False]*m for _ in range(n)]
    rtn = 0
    for i in range(n):
        for j in range(m):
            if 0 < swimming[i][j] < k and not visited[i][j]:
                rtn += bfs(i, j, k)
    result += rtn
print(result)
# bfs
# 높이를 기준으로 하나씩 채워간다 !
# 둘러쌓인 것들이 현재것보다 크면 현재 것에 더 해준다.

'''
5 5
59995
95549
94449
95449
88888
'''