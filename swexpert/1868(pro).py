# dfs
from collections import deque


def checkit(r, c):
    for k in range(8):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < N and 0 <= nc < N :
            if matrix[nr][nc] == '*':
                return 1
    return 0


def BFS(r, c):
    # DFS X 깊이가 너무 깊어진다.
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        rr, cc = q.popleft()
        for i in range(8):
            nr = rr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                if matrix[nr][nc] == 0:
                    q.append((nr, nc))



for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    zero_list = []
    for i in range(N):
        for j in range(N):
            # 지뢰를 찾아준다.
            if matrix[i][j] == '.':
                matrix[i][j] = checkit(i, j)
            # 주변에 지뢰가 없다면
            if matrix[i][j] == 0:
                zero_list.append((i, j))
    ans = 0 # 클릭횟수
    # 방문여부 꼭 체크
    visited = [[False] * N for _ in range(N)]
    # 주변에 지뢰가 하나도 없는 값들을 먼저 클릭
    for r,c in zero_list:
        if visited[r][c]:
            continue
        BFS(r, c)
        ans += 1

    # 나머지 지뢰가 아닌 칸들을 클릭
    for i in range(N):
        for j in range(N):
            # 방문하지 않고 지뢰가 아닌 값들 숫자도 없는
            if not visited[i][j] and matrix[i][j] != '*':
                ans += 1

    print(f'#{tc} {ans}')
