# 등산로 조정 다시 풀기
import sys

sys.stdin = open('input16.txt', 'r')


def dfs(r, c, k, cnt):
    global large_step
    if cnt + 1 > large_step:
        large_step = cnt + 1

    for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if hiking[nr][nc] < hiking[r][c]:
                # 숫자 안빼고 작을 때
                visited[nr][nc] = True
                dfs(nr, nc, k, cnt + 1)
                visited[nr][nc] = False
            elif hiking[nr][nc] - k < hiking[r][c]:
                # 딱 한곳만 정해서 그곳을 뺸다. 최대 k 깊이 만큼
                # 갈 수 있는 만큼만 깎아라
                origin = hiking[nr][nc]
                visited[nr][nc] = True
                # 현재칸 보다 한 칸만 작아도 되니깐 
                hiking[nr][nc] = hiking[r][c] - 1
                dfs(nr, nc, 0, cnt + 1)
                hiking[nr][nc] = origin
                visited[nr][nc] = False


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    hiking = [list(map(int, input().rsplit())) for _ in range(n)]
    max_num = max(map(max, hiking))
    first_step = []
    large_step = -1
    for i in range(n):
        for j in range(n):
            # 가장 높은 봉우리에서 시작
            if hiking[i][j] == max_num:
                first_step.append((i, j))
    for i in first_step:
        r, c = i[0], i[1]
        visited = [[False] * n for _ in range(n)]
        visited[r][c] = True
        dfs(r, c, k, 0)
    print(f'#{tc} {large_step}')

# 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 함
# 높이가 같은 지형도 안됨
# 딴 한 곳을 정해서 최대 k 깊이 만큼 지형을 깎는 공사
