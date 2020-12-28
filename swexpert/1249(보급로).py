import sys
import collections
sys.stdin = open('input5.txt', 'r')


def bfs():
    q = collections.deque()
    q.append([0, 0])
    arr[0][0] = 0   # 시작점 복구
    while q:
        i, j = q.popleft()
        for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nx, ny = dx+i, dy+j
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > arr[i][j] + matrix[nx][ny]:    # 모든 경로를 다 지나가면서 최소값을 찾을수도 있음. 왔던 경로는 다시 안갈수도 있고
                    arr[nx][ny] = arr[i][j] + matrix[nx][ny]
                    q.append([nx, ny])


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().rstrip())) for _ in range(N)]
    arr = [[1000000000000] * N for _ in range(N)]
    bfs()
    print(f'#{tc} {arr[N-1][N-1]}')




# dijastra

# import heapq
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     road = [list(map(int,input())) for _ in range(N)]
#     #최소비용을 저장하기 위한 배열
#     INF = float('inf')
#     min_path = [[INF] * N for _ in range(N)]
#
#     def dijkstra():
#         delta = [(-1,0),(1,0),(0,-1),(0,1)]
#         queue = list()
#         min_path[0][0] = 0
#         heapq.heappush(queue,(min_path[0][0],0,0))
#         while queue:
#             cw,cr,cc = heapq.heappop(queue)
#             #최소 비용 가지고 왔으니까....
#             #현재 위치에서 갈 수 있는 경로 넣어주기
#             for dr,dc in delta:
#                 nr,nc = cr+dr,cc+dc
#                 if 0<= nr < N and 0 <= nc< N:
#                     #현재 위치의 누적 가중치 + 다음 위치의 깊이
#                     tmp_v = cw + road[nr][nc]
#                     if min_path[nr][nc] > tmp_v:
#                         min_path[nr][nc] = tmp_v
#                         heapq.heappush(queue,(min_path[nr][nc],nr,nc))
#         return min_path[N-1][N-1]
#     result = dijkstra()
#     print("#{} {}".format(tc,result))