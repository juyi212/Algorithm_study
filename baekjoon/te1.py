# 뱀 문제 연습
import sys
from collections import deque


def check():
    dr = [-1, 0, 1, 0]  # 시계 방향
    dc = [0, 1, 0, -1]
    snakes = deque()
    snakes.append((0, 0))
    nd = 1
    nr, nc = 0, 0
    matrix[nr][nc] = 1
    t = 1
    # 머리랑 꼬리 생각해야함
    # 뱀의 길이를 queue에 담아서 확인해준다
    # 맨 처음은 꼬리, 맨 뒤는 머리로 생각하고
    while True:
        nr, nc = nr + dr[nd], nc + dc[nd]
        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] != 1:
            if matrix[nr][nc] == 2:  # 사과가 있다면
                # 그칸에 있떤 사과가 없어지고 꼬리는 움직이지 않는다.
                matrix[nr][nc] = 1
                snakes.append((nr, nc))
            else:
                matrix[nr][nc] = 1
                snakes.append((nr, nc))
                tailf, taile = snakes.popleft()
                matrix[tailf][taile] = 0
            if t in snake_dir:
                if snake_dir[t] == 'L':
                    nd = (nd - 1) % 4
                else:
                    nd = (nd + 1) % 4
            t += 1
        else:
            # 범위가 넘어가거나 자신과 부딪힌다면
            return t


N = int(sys.stdin.readline())  # 보드의 크기
K = int(sys.stdin.readline())  # 사과의 개수
matrix = [[0] * N for _ in range(N)]
for _ in range(K):
    f, e = map(int, sys.stdin.readline().split())
    # 맨위 좌측이 1행 1열이라 했으므로
    matrix[f - 1][e - 1] = 2  # 사과는 2

L = int(sys.stdin.readline())
snake_dir = {}
for _ in range(L):
    time, dir = sys.stdin.readline().split()
    snake_dir[int(time)] = dir
print(check())
