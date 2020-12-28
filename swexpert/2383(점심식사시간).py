from itertools import combinations
from collections import deque



def check(n_people, n_stair):
    times = []
    if len(n_people) == 0:
        return 0
    for pr, pc in n_people:
        times.append(abs(pr-n_stair[0])+ abs(pc - n_stair[1]))
    # 시간순으로
    times.sort()
    leng2 = len(times)
    time = 0
    # 계단에 도착하고 내려가는 것 까지. 계단에는 3명이상 있으면 안된다는 거 유의
    # 나오고 들어가는 것을 어떻게 표현할 것인가..
    stair = []
    completed = []
    while len(completed) != leng2:
        time += 1
        while stair and stair[0] == n_stair[2]:
            completed.append(stair.pop(0))
            while times and times[0] < time and len(stair) < 3:
                times.pop(0)
                stair.append(0)

        for i in range(len(stair)):
            stair[i] += 1

        while times and times[0] <= time and len(stair) < 3:
            times.pop(0)
            stair.append(0)

    return time


# 계단 두 곳을 comb로 두 그룹으로 나눠서 하나씩 비교하기
for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    peoples =[]
    stairs = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1: # 사람일 경우
                peoples.append((i, j))
            elif matrix[i][j] > 1:
                stairs.append((i, j, matrix[i][j]))

    result = 100000000
    for i in range(len(peoples)+1):
        for comb in combinations(peoples, i):
            group1 = list(comb)
            group2 = list(set(peoples)- set(comb))
            # 두 개의 그룹으로 나눔
            result = min(result, max(check(group1, stairs[0]), check(group2, stairs[1])))
    print(f'#{tc} {result}')

'''
10
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
5
0 0 1 1 0
0 0 1 0 2
0 0 0 1 0
0 1 0 0 0
1 0 5 0 0
'''