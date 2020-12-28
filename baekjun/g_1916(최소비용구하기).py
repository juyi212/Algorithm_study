import sys
import heapq


def check(start, end, cost):
    q = []
    heapq.heappush(q, [0, start])
    while q:
        dis, l_node = heapq.heappop(q)

        if cost[l_node] < dis:  # 연결된 노드를 검사하기 전에
            # 해당경로까지의 경로가 이전보다 길다면 탐색 x
            continue

        for d, x in matrix[l_node]: # 연결된 노드 탐색
            d += dis    # 이전거리와 현재 연결된 노드의 거리를 더해서
            if d < cost[x]: # 거리를 비교 , 거리가 이전보다 짧으면 갱신
                cost[x] = d
                heapq.heappush(q, [d, x])   # 우선순위 큐에 넣어준다.


N = int(sys.stdin.readline())   # 도시의 개수
M = int(sys.stdin.readline())   # 버스의 개수

matrix = [[] for _ in range(N+1)]

for i in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    matrix[s].append([c, e])

start, end = map(int, sys.stdin.readline().split())

INF = 1000000000
cost = [INF for _ in range(N+1)]
cost[start] = 0

check(start, end, cost)
print(cost[end])
