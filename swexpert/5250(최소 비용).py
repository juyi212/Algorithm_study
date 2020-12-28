from _collections import deque


def check(r, c, matrix, weight):
    queue = deque()
    queue.append((r, c))
    while queue:
        x, y = queue.popleft()
        for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < N:
                plus = matrix[nx][ny] - matrix[x][y]
                if plus < 0:
                    plus = 0

                tmp = 1 + plus
                # nx,ny는 바로 갔을 때 비용
                if weight[nx][ny] > weight[x][y] + tmp:  # tmp 는 돌아갔을 때의 최소 비용이고
                    weight[nx][ny] = (tmp + weight[x][y])
                    queue.append((nx, ny))

    return weight


for tc in range(1, int(input()) + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    weight = [[1000000] * N for _ in range(N)]  # 가중치를 표시할 행렬
    weight[0][0] = 0  # 첫 값을 0으로 초기화
    result = check(0, 0, matrix, weight)
    print('#{} {}'.format(tc, result[N - 1][N - 1]))
