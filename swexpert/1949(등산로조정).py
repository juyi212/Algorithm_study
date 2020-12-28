import sys
sys.stdin = open('input16.txt','r')


def check(r, c, k, cnt):
    global total_len

    if total_len < cnt +1:
        total_len = cnt +1

    for dr, dc in ([1, 0],[-1, 0],[0, 1],[0, -1]):
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 숫자 안빼고 그냥 깎을 때
            if matrix[nr][nc] < matrix[r][c]:
                visited[nr][nc] = True
                check(nr, nc, k, cnt+1)
                visited[nr][nc] = False

            elif matrix[nr][nc] - k < matrix[r][c]:
                origin = matrix[nr][nc]
                # 하나씩 뺴준다 최대 깊이가 k 이기 때문에
                matrix[nr][nc] = matrix[r][c] - 1
                visited[nr][nc] = True

                check(nr, nc, 0, cnt+1)
                visited[nr][nc] = False
                matrix[nr][nc] = origin


for tc in range(1, int(input())+1):
    N, K = map(int, input().split()) # 크기, 최대 깎을 수 있는 수
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 가장 높은 봉우리가 있는 위치를 담아두고
    # 주위에 있는 숫자 모두를 탐색하면서 하나씩 깎어보고 결정.
    # 하나씩 delta를 넣어서 확인
    total_len = -1
    max_num = max(map(max, matrix))
    li = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_num:
                li.append([i, j])

    for i in li:
        visited = [[False] * N for _ in range(N)]
        visited[i[0]][i[1]] = True
        check(i[0], i[1], K, 0)

    print(f'#{tc} {total_len}')