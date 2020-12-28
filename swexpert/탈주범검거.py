import sys
from collections import deque

sys.stdin = open('input14.txt', 'r')

check = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}


def bfs(r, c, l):
    q = deque()
    q.append([r, c, l])
    here = set()
    here.add((r, c))
    visited[r][c] = True

    while q:
        x, y, cnt = q.popleft()
        if cnt == 1:
            break
        for dx, dy in check[matrix[x][y]]:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] != 0:
                if (-dx, -dy) in check[matrix[nx][ny]]: # 연결되어있는지 체크
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt - 1])
                    here.add((nx, ny))

    if here:
        return len(here)


for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())  # 세로, 가로 크기, 맨홀이 위치한 장소, 탈출 후 소요된 시간
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    print('#{} {}'.format(tc, bfs(R, C, L)))
