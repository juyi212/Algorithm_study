import sys
import heapq


def dijkstra(k, matrix, weight):
    q = []
    heapq.heappush(q, [0, k])
    while q:
        dis, end = heapq.heappop(q)

        if weight[end] < dis:
            continue

        for d, x in matrix[end]:
            d += dis
            if d < weight[x]:
                weight[x] = d
                heapq.heappush(q, [d, x])   # 최단거리 기준으로 정점을 배열한다
                # 아직 방문하지 않은 정점 중 시작지점으로부터의 거리가 가장 가까운 점을 찾는 과정을 간단하게 해줌

    return weight


V, E = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

INF = sys.maxsize
matrix = [[] for _ in range(V+1)]   # 인접리스트

for i in range(E):
    s, e, w = map(int, sys.stdin.readline().split())    # 백준 realine 필수
    matrix[s].append([w, e])

weight =[INF for _ in range(V+1)]
weight[k] = 0

result = dijkstra(k, matrix, weight)

for i in range(1, V+1):
    if result[i] != INF:
        print(result[i])
    else:
        print('INF')