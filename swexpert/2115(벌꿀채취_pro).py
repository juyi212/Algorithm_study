import sys
sys.stdin = open('input15.txt','r')


# def choose(r, c):
#     global first, second
#     honey = arr[r][c:c+M] # 구하는 벌통 짜르기
#     max_cost = 0
#
#     for i in range(1 << M):
#         sum_honey = sum_cost = 0
#         for j in range(M):
#             if i & (1 << j):
#                 sum_honey += honey[j]
#                 sum_cost += honey[j]**2
#         if sum_honey <= C:
#             max_cost = max(max_cost, sum_cost)
#
#     if max_cost > first[0]:
#         # r 벌통의 행
#         if r == first[1] and c < first[2] + M: # 겹친다.
#             first = [max_cost, r, c]
#         else:   # 겹치지 않는다.
#             second = first[:]
#             first = [max_cost, r, c]
#     elif max_cost > second[0]:
#         if r != first[1] or c >= first[2]+M:
#             second = [max_cost, r, c]


def calc(idx, sum_honey, sum_cost):
    global max_cost2
    if sum_honey > C:
        return

    max_cost2 = max(max_cost2, sum_cost)

    for i in range(idx, M):
        calc(i+1, sum_honey+honey2[i], sum_cost+honey2[i]**2)


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    first = [0, 0, 0]
    second = [0, 0, 0]

    honey_list = []
    for i in range(N):
        for j in range(N-M+1):
            # choose(i,j) # 가로로 연속된 통을 뽑기때문에 모두 실행해볼 필요는 없음
            honey2 = arr[i][j:j+M]
            max_cost2 = 0
            calc(0,0,0)
            honey_list.append((max_cost2, i, j))

    honey_list.sort(reverse=True)
    first2 = honey_list.pop(0) # 항상 가장 큰 값은 앞에 있다.
    for cost, r, c in honey_list:
        if r == first2[1] and first2[2] - M < c < first[2] + M: continue

        second2 = [cost, r, c]  # first 에 겹치지않고 다음 큰 값
        break

    # print(f'#{tc} {first[0] + second[0]}')
    print(f'#{tc} {first2[0] + second2[0]}')