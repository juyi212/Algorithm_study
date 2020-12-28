
# 약간의 누적합
def dijkstra(start, adj, weight):
    U = set()
    # 1. 현재 방문하지 않은 정점중, 최소비용으로 방문할 수 있는 정점 방문
    # 2. 새로운 정점에 방몬하고 나서, 그 정점으로 부터 모든 갈 수 있는
    #    모든 정점의 비용을 확인해서, 기존 최소 비용보다 더 작다면 수정.

    while len(U) < V + 1:
        min_w = INF
        min_idx = -1
        for i in range(V + 1):
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i

        U.add(min_idx)  # 방문

        for i in range(V + 1):
            if i not in U:
                tmp = min_w + adj[min_idx][i]   # 거처서 갈 때의 값
                if weight[i] > tmp:
                    weight[i] = tmp

    return weight


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    INF = float('inf')
    adj = [[INF] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    start = 0
    weight = [INF] * (V + 1)
    weight[start] = 0
    result = dijkstra(start, adj, weight)
    print('#{} {}'.format(tc, result[-1]))
