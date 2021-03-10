# import sys
# from collections import deque
#
#
# def bfs(first_point):
#     while q:
#         z, r, c = q.popleft()
#         for dz, dr, dc in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
#             nz, nr, nc = z + dz, r + dr, c + dc
#             if 0 <= nz < H and 0 <= nr < N and 0 <= nc < M and boxes[nz][nr][nc] == 0:
#                 q.append((nz, nr, nc))
#                 boxes[nz][nr][nc] = boxes[z][r][c] + 1
#
# # 3차원
# # 위 아래 왼 오 앞 뒤
# M, N, H = map(int, sys.stdin.readline().rsplit())  # 가로 세로 쌓아 올리는 수
#
# boxes = [[list(map(int, sys.stdin.readline().rsplit())) for _ in range(N)] for _ in range(H)]
# q = deque()
# for i in range(H):
#     for j in range(N):
#         for z in range(M):
#             if boxes[i][j][z] == 1:
#                 q.append((i, j, z))
# if len(q) == N * H * M:
#     print(0)
#     exit(0)
# else:
#     bfs(q)
#     max_num = 0
#     for i in range(H):
#         for j in range(N):
#             for z in range(M):
#                 if boxes[i][j][z] == 0:
#                     print(-1)
#                     exit()
#                 # cnt로 해도됨
#                 max_num = max(max_num, boxes[i][j][z])
#     print(max_num-1)

# 시간 줄이는 방법
import sys
from collections import deque


def check(a, q):
    cnt = 0
    while q:
        size = len(q)
        if size == 0:
            break
        cnt += 1
        for i in range(size):
            z, x, y = q.popleft()
            if x - 1 >= 0 and a[z][x - 1][y] == 0:
                q.append((z, x - 1, y))
                a[z][x - 1][y] = 1
            if x + 1 < n and a[z][x + 1][y] == 0:
                q.append((z, x + 1, y))
                a[z][x + 1][y] = 1
            if y - 1 >= 0 and a[z][x][y - 1] == 0:
                q.append((z, x, y - 1))
                a[z][x][y - 1] = 1
            if y + 1 < m and a[z][x][y+1] == 0:
                q.append((z,x,y+1))
                a[z][x][y+1] = 1
            if z -1  >= 0 and a[z-1][x][y] == 0:
                q.append((z-1, x, y))
                a[z-1][x][y] = 1
            if z+1 < h and a[z+1][x][y] == 0:
                q.append((z+1, x, y))
                a[z+1][x][y] = 1
    return cnt


def solve(a):
    q = deque()
    for i in range(h):
        for j in range(n):
            for z in range(m):
                if a[i][j][z] == 1:
                    q.append((i, j, z))
    res = check(a, q)
    for i in range(h):
        for j in range(n):
            for z in range(m):
                if a[i][j][z] == 0:
                    return -1
    return res-1


m, n, h = map(int, sys.stdin.readline().split())
a = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for i in range(h)]

print(solve(a))

#
#
# def bfs(a, haveTo):
#     cnt = 0
#     while True:
#         size = len(haveTo)
#         if size == 0:
#             break
#         cnt += 1
#         for _ in range(size):  # 모두다 펼펴
#             z, x, y = haveTo.popleft()
#             if x - 1 >= 0 and a[z][x - 1][y] == 0:  # up
#                 a[z][x - 1][y] = 1
#                 haveTo.append((z, x - 1, y))
#             if x + 1 < n and a[z][x + 1][y] == 0:  # down
#                 a[z][x + 1][y] = 1
#                 haveTo.append((z, x + 1, y))
#             if y - 1 >= 0 and a[z][x][y - 1] == 0:  # down
#                 a[z][x][y - 1] = 1
#                 haveTo.append((z, x, y - 1))
#             if y + 1 < m and a[z][x][y + 1] == 0:  # down
#                 a[z][x][y + 1] = 1
#                 haveTo.append((z, x, y + 1))
#             if z - 1 >= 0 and a[z - 1][x][y] == 0:  # Upstair
#                 a[z - 1][x][y] = 1
#                 haveTo.append((z - 1, x, y))
#             if z + 1 < h and a[z + 1][x][y] == 0:  # downStair
#                 a[z + 1][x][y] = 1
#                 haveTo.append((z + 1, x, y))
#     return cnt
#
#
# def solve(a):
#     haveTo = deque()
#     for i in range(h):
#         for j in range(n):
#             for k in range(m):
#                 if a[i][j][k] == 1:
#                     haveTo.append((i, j, k))
#     res = bfs(a, haveTo)
#     for i in range(h):
#         for j in range(n):
#             for k in range(m):
#                 if a[i][j][k] == 0:
#                     print(-1)
#                     return 0
#     print(res - 1)
#
#
