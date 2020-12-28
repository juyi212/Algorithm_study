from collections import deque


def push():
    if S == 'up':
        for i in range(N):
            q = deque()
            for j in range(N):
                if matrix[j][i]:
                    q.append(matrix[j][i])
                    matrix[j][i] = 0

            idx = 0
            while q:
                if len(q) > 1:
                    a, b = q.popleft(), q.popleft()
                    if a == b:
                        matrix[idx][i] = a + b
                    else:
                        matrix[idx][i] = a
                        q.appendleft(b)
                    idx += 1
                else:
                    matrix[idx][i] = q.popleft()

    elif S == 'down':
        for i in range(N):
            q = deque()
            for j in range(N-1, -1, -1):
                if matrix[j][i]:
                    q.append(matrix[j][i])
                    matrix[j][i] = 0
            idx = N-1
            while q:
                if len(q) > 1:
                    a, b = q.popleft(), q.popleft()
                    if a == b:
                        matrix[idx][i] = a + b
                    else:
                        matrix[idx][i] = a
                        q.appendleft(b)
                    idx -= 1
                else:
                    matrix[idx][i] = q.popleft()

    elif S == 'left':
        for i in range(N):
            q = deque()
            for j in range(N):
                if matrix[i][j]:
                    q.append(matrix[i][j])
                    matrix[i][j] = 0
            idx = 0
            while q:
                if len(q) > 1:
                    a, b = q.popleft(), q.popleft()
                    if a == b:
                        matrix[i][idx] = a+b
                    else:
                        matrix[i][idx] =a
                        q.appendleft(b)
                    idx += 1
                else:
                    matrix[i][idx] = q.popleft()

    else:
        for i in range(N):
            q = deque()
            for j in range(N-1, -1, -1):
                if matrix[i][j]:
                    q.append(matrix[i][j])
                    matrix[i][j] = 0
            idx = N-1
            while q:
                if len(q) > 1:
                    a, b = q.popleft(), q.popleft()
                    if a == b:
                        matrix[i][idx] = a+b
                    else:
                        matrix[i][idx] =a
                        q.appendleft(b)
                    idx -= 1
                else:
                    matrix[i][idx] = q.popleft()


# direction = {'left': (0,-1), 'right': (0, 1), 'up': (1, 0), 'down':(-1, 0)}
for tc in range(1, int(input())+1):
    # 시뮬레이션 문제
    # 회전으로 풀 수 있음
    N, S = input().split()
    N = int(N)
    matrix = [list(map(int, input().split())) for _ in range(N)]

    push()

    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])






'''
2
5 left
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
'''