# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우 -> 바라보는 방향에서 한칸 후진
# 뒷쪽방향이 벽이라 후진도 할 수 없는 경우 -> 작동을 멈춘다

import sys
from collections import deque

def bfs(r, c, d):
    q = deque()
    q.append((r, c, d))
    matrix[r][c] = 2
    cnt = 1

    while q:
        r, c, d = q.popleft()
        td = d
        for i in range(4):
            # 변수 설정에 유의하자
            td = (td + 3) % 4
            nr, nc = r+dr[td], c+dc[td]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
                cnt += 1
                matrix[nr][nc] = 2
                q.append((nr, nc, td))
                break

            if i == 3:
                # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
                nd = (d + 2) % 4
                # 잠시 뒤로 가는건 일시적 -!
                nr, nc = r+dr[nd], c+dc[nd]
                if matrix[nr][nc] == 1:
                    return cnt
                q.append((nr, nc, d))




N, M = map(int, sys.stdin.readline().split())  # 크기
r, c, d = map(int, sys.stdin.readline().split())  # 청소기가 있는 좌표, 방향
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

print(bfs(r, c, d))