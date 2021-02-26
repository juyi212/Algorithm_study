import sys
from collections import deque

def check(direction):
    if direction == 'L':
        # 왼쪽
        return

    elif direction == 'D':
        pass

def bfs(r, c):
    # 뱀은 매 초마다 이동
    # 시작 위치 0,0 에서 1초 늘어났을 때 머리가 0,1 에 위치
    # 만약에 그 위치에 사과가 있다 ?
    # 없다 ?
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    snake = deque()
    snake.append((r, c))
    time = 1
    d = 0
    while True:
        r, c = r + dr[d], c + dc[d]
        if 0 <= r < N and 0 <= c < N and matrix[r][c] != 2:
            if matrix[r][c] == 1: # 사과를 만났을때
                snake.append((r, c))
                matrix[r][c] = 2

            # 꼬리가 윽시 길수도있는디
            elif matrix[r][c] == 0: # 사과 x
                matrix[r][c] = 2
                snake.append((r,c))
                tailr, tailc = snake.popleft()
                matrix[tailr][tailc] = 0

            if time in snake_dir.keys():
                if snake_dir[time] == 'L':
                    d = (d+3) % 4
                else:
                    d = (d+1) % 4
            time += 1
        else:
            # 밖을 벗어났을 때
            return time




N = int(sys.stdin.readline())  # 보드의 크기
K = int(sys.stdin.readline())  # 사과의 개수
matrix = [[0] * N for _ in range(N)]
# apples = []
for _ in range(K):
    f, e = map(int, sys.stdin.readline().split())
    # 이런 말이어디숨
    matrix[f-1][e-1] = 1

L = int(sys.stdin.readline())  # 뱀 방향 변환 횟수
snake_dir = {}
for _ in range(L):
    time, dir = sys.stdin.readline().split()
    snake_dir[int(time)] = dir

matrix[0][0] = 2
print(bfs(0, 0))
