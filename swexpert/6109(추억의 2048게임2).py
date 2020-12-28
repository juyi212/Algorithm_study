from collections import deque

def dir():
    # 시계방향으로 90도
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = matrix[N-1-j][i]

    return tmp


def push():
    # 행 left 기준
    for i in range(N):
        q = deque()
        for j in range(N):
            if matrix[i][j]:
                q.append(matrix[i][j])
                # 넣어준 후 0으로 초기화
                matrix[i][j] = 0
        idx = 0
        while q:
            if len(q) > 1:
                # 두 개씩 빼서 확인
                a, b = q.popleft(), q.popleft()
                if a == b:
                    matrix[i][idx] = a + b
                else:
                    # 같지 않으면 처음 것만 넣어주고
                    matrix[i][idx] = a
                    # 뒤에 값은 다시 q로 넣어준다
                    q.appendleft(b)
                # 같던 같지 않던 idx +
                idx += 1
            else:
                # 1개만 남았을 때는 빼서 넣어준다
                matrix[i][idx] = q.popleft()



# left 기준으로 방향 설정 해줌 2차원 배열 돌리기
direction = {'left': (0, 0) , 'right': (2, 2), 'up': (3, 1) , 'down': (1, 3)}
for tc in range(1, int(input())+1):
    # 시뮬레이션 문제
    # 회전으로 풀 수 있음
    N, S = input().split()
    N = int(N)
    matrix = [list(map(int, input().split())) for _ in range(N)]
    v1,v2 = direction[S]

    for i in range(v1):
        matrix = dir()
    push()
    for i in range(v2):
        matrix = dir()

    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])






'''
2
5 up
4 8 2 4 0
4 4 2 0 8
8 0 2 4 4
2 2 2 2 8
0 2 2 0 0
2 down
16 2
0 2
'''