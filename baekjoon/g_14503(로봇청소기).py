import sys
from collections import deque


def solve(r, c, d):
    cnt = 1
    matrix[r][c] = 2
    q = deque([[r, c, d]])
    while q:
        r, c, d = q.popleft()
        tmp = d
        for i in range(4):
            # 바라보는 방향의 왼쪽 부터
            tmp = (tmp + 3) % 4
            nr, nc = r + dr[tmp], c + dc[tmp]
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
                cnt += 1
                matrix[nr][nc] = 2
                q.append([nr, nc, tmp])
                break


            # 네 방향 모두 청소가 이미 되어 있거나
            elif i == 3:
                # 뒤로 후진을 하고 2번으로 돌아간다. 원래 방향을 갖고 d 유지
                nd = (d + 2) % 4
                nr, nc = r + dr[nd], c + dc[nd]
                # 뒤에 벽
                if matrix[nr][nc] == 1:
                    return cnt
                q.append([nr, nc, d])


N, M = map(int, sys.stdin.readline().split())  # 크기
r, c, d = map(int, sys.stdin.readline().split())  # 청소기가 있는 좌표, 방향
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# dfs(r, c, d)
print(solve(r, c, d))


