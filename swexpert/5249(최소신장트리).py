def prim(adj, start):
    weight = [1000000] * (V + 1)
    mst = [0] * (V + 1)
    weight[start] = 0   # 초기화 필수
    result = 0

    for _ in range(V + 1):
        # 현재 갈 수 있는 경로 중 가장 가중치가 작은 경로를 선택
        min_w = 10000000
        min_v = 0

        for i in range(V + 1):
            if mst[i] == 0 and weight[i] < min_w:
                min_w = weight[i]
                min_v = i

        mst[min_v] = 1  # 체크체크
        result += min_w

        for i in range(V + 1):
            if 0 < adj[min_v][i] < weight[i] and not mst[i]:
                weight[i] = adj[min_v][i]

    return result


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
        adj[e][s] = w

    print('#{} {}'.format(tc, prim(adj, 0)))



'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

'''

# kruskal 로 풀어보기 겨수님 풀이
#
# def make_set(x):
#     p[x] = x
#
#
# def find_set(x):
#     if p[x] != x:
#         p[x] = find_set(p[x])
#     return p[x]
#
#
# def union(x, y):
#     p[find_set(y)] = find_set(x)
#
#
# for tc in range(1, int(input()) + 1):
#     V, E = map(int, input().split())
#
#     edges = [list(map(int, input().split())) for _ in range(E)]
#
#     p = [0] * (V + 1)
#
#     # 가중치 정렬
#
#     edges = sorted(edges, key=lambda x: x[2])
#     for i in range(V + 1):
#         make_set(i)
#
#     ans = 0
#     cnt = 0  # 간선을 v개 선택을 해야하니깐
#     idx = 0
#
#     while cnt < V:
#         x = edges[idx][0]
#         y = edges[idx][1]
#
#         if find_set(x) != find_set(y):  # 같은 그룹이아닐때만 union
#             union(x, y)
#             cnt += 1  # 간선을 선택 한것임
#             ans += edges[idx][2]
#         idx += 1
#     print(ans)