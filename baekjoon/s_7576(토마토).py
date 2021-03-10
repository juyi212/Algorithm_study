import sys
import copy
from collections import deque


def bfs(first):
    q = deque((first))
    # 상하좌우 보면서 익은 거 체크
    # queue에 넣어주기
    while q:
        r, c, cnt = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if boxes[nr][nc] == 0:
                    q.append((nr, nc, cnt + 1))
                    boxes[nr][nc] = 1
                    visited[nr][nc] = True

    for i in range(N):
        if boxes[i].count(0):
            return -1
    return cnt


M, N = map(int, sys.stdin.readline().rsplit())

boxes = [list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# 1 익은 토마토, 0 안익은거 , -1 토마토가 들어있지않은 칸
answer = 1000000000
first = []
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            # 처음에 동시에 익은거 찾기
            first.append((i, j, 0))
            visited[i][j] = True
print(bfs(first))
