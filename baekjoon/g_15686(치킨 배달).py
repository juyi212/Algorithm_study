import sys
# from itertools import combinations
#
#
# def checkit(ch, homes):
#     # 각 집마다의 치킨집 과의 거리
#     ret = 0
#     for home in homes:
#         min_d = 10000000000
#         for c in ch:
#             # 최소
#             distance = abs(c[0]-home[0])+abs(c[1]-home[1])
#             min_d = min(min_d, distance)
#         ret += min_d
#     return ret
#
#
#
# N, M = map(int, sys.stdin.readline().split()) # n개의 도시 정보, m 개 고름
# matrix = [list(map(int, input().split())) for _ in range(N)]
#
# homes = []
# chicken = []
# for i in range(N):
#     for j in range(N):
#         if matrix[i][j] == 1:
#             homes.append((i, j))
#         if matrix[i][j] == 2:
#             chicken.append((i, j))
# res = []
# # 치킨 집중에 m개 고르기 조합
# res = combinations(chicken, M)
#
# # for i in range(1, M+1):
# #     tmp = list(combinations(chicken, i))
# #     res += tmp
#
# result = 100000000
# for i in res:
#     re = checkit(i, homes)
#     result = min(result, re)
# print(result)

# dfs 로 풀어보기

def dfs(idx, selected):
    global answer

    if idx > len(chicken):
        return
    if selected == M:
        sum_d = 0
        for home in homes:
            min_d = 10000000000
            for ch_idx, value in enumerate(chicken):
                if not check[ch_idx]:
                    continue
                min_d = min(min_d, (abs(value[0] - home[0])+abs(value[1]- home[1])))
            sum_d += min_d
        answer = min(sum_d, answer)
        return

    # 선택 된 것과 안된 것으로 나눔
    check[idx] = True
    dfs(idx+1, selected+1)
    check[idx] = False
    dfs(idx+1, selected)


N, M = map(int, sys.stdin.readline().split()) # n개의 도시 정보, m 개 고름
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 100000000000
homes = []
chicken = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            homes.append((i, j))
        if matrix[i][j] == 2:
            chicken.append((i, j))

check = [False] * (len(chicken) + 1)
dfs(0, 0)
print(answer)
