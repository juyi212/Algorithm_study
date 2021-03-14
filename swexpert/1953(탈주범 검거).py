# bfs
import sys
from collections import deque

sys.stdin = open('input18.txt', 'r')

tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}


def bfs(fr, fc, l):
    q = deque()
    q.append((fr, fc, 1))
    ans = 1
    visited[fr][fc] = True
    while q:
        r, c, cnt = q.popleft()
        if cnt == l:
            break
        for dr, dc in tunnel[matrix[r][c]]:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < m:
                if (-dr, -dc) in tunnel[matrix[nr][nc]]:
                    # 연결된 통로인지 확인해줘야함 !!!!!!
                    if matrix[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc, cnt + 1))
                        visited[nr][nc] = True
                        ans += 1
    return ans


for tc in range(1, int(input()) + 1):
    n, m, fr, fc, l = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    print(f'#{tc} {bfs(fr, fc, l)}')
