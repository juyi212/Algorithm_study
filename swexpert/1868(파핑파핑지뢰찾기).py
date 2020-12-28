# dfs
from collections import deque

def checkit(r, c):
    #   8 방향으로 주변에 지뢰가 하나도 없으면 체크
    global cnt
    nxt_li = []
    for k in range(8):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N :
            if matrix[nr][nc] == '.':
                nxt_li.append((nr, nc))
            else:
                break
    else:
        if nxt_li:
            matrix[r][c] = 0
            cnt += 1
            ch = True
            spread(nxt_li)


def spread(nxt_li):
    q = deque(nxt_li)
    while q:
        x, y = q.popleft()
        matrix[x][y] = 0
        next_next = []
        for k in range(8):
            nr, nc = x + dr[k], y + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] == '.':
                    next_next.append((nr, nc))
                else:
                    break
        else:
            if next_next:
                spread(next_next)


def remainder():
    global cnt

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                cnt += 1


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    cnt = 0
    ch = False
    dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(N):
        for j in range(N):
            # 최초로 클릭할지 말지 결정
            if matrix[i][j] == '.':
                checkit(i, j)
    else:
        # 나머지 부분들
        remainder()

    print(f'#{tc} {cnt}')
