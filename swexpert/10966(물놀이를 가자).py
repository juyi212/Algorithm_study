from collections import deque

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    visited = [[-1] * m for _ in range(n)]
    queue = []
    for i in range(n):
        temp = list(input())
        for j in range(m):
            if temp[j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0
    # 물 위치 받는다
    q = deque(queue)
    ans = 0
    while q:
        r, c = q.popleft()
        # 시작 정점부터 거쳐가는 간선의 수가 같은 순서로 탐색 bfs
        # 하나씩 탐색을 한다. 처음 물 위치가 먼저 popleft 되기때문에 append되어도 상관 x
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1 # r,c 노드로 부터 nr, nc 노드 탐색
                ans += visited[nr][nc]
    print(f'#{tc} {ans}')

# 시간 초과
# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     matrix = [list(input()) for _ in range(n)]
#     # 물인 곳을 따로 저장
#     water = []
#     # 땅인 곳도 저장을 해서
#     ground = []
#     # 하나씩 봐주면서 최소인걸 고른다
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 'W':
#                 water.append((i, j))
#             else:
#                 ground.append((i, j))
#     answer = 0
#     for g in ground:
#         min_block = 1000
#         for w in water:
#             block = abs(g[0]-w[0])+abs(g[1]- w[1])
#             if min_block > block:
#                 min_block = block
#         answer += min_block
#     print(f'#{tc} {answer}')
'''
3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL
'''
