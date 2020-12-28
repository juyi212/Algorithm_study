import sys
from collections import deque

def check():
    cnt, time = 0, 0
    q = deque()
    # 상하좌우에 0,-1 이 있음 c
    while True:
        result = []
        q.append((0, 0))
        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = -1
                        q.append((nr, nc))
                    elif matrix[nr][nc] == 1:
                        matrix[nr][nc] = -1     # 방문표시
                        result.append((nr, nc))     # c 값을 체크

        if not result:  # 결과 값 안에 아무것도 없으면 멈춰
            break

        time += 1
        cnt = len(result)

        for n in range(R):  # 탐색 해준 값들 0으로 초기화
            for m in range(C):
                if matrix[n][m] == -1:
                    matrix[n][m] = 0

    return time, cnt


R, C = map(int, sys.stdin.readline().split())
matrix=[list(map(int, sys.stdin.readline().split())) for _ in range(R)]
t, cn = check()
print(t)
print(cn)

# 이 코딩에서는 양끝 고려를 하지 않았다.
# 1밖에 있는 0인부분과 동일시 여김
# 값이 1인 것중에서 좌우상하 중에 -1 이나 0이 c이고 지워주면 됨.
# 깊이로 count
# 마지막 직전에는 몇개 남았는지 알아야함 so, 지워진거 count 해야함.