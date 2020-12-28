import sys
sys.stdin = open('input9.txt', 'r')


def check():
    while True:
        for i in range(N):
            if times[i][0] < result[-1][-1]:
                visited[i] = 1
        if 0 not in visited:
            break
        value = 10000000
        idx = 0
        for i in range(N):
            if visited[i] == 0 and times[i][0] >= result[-1][-1] and times[i][1] < value:
                value = times[i][0]
                idx = i
        result.append(times[idx])


for tc in range(1, int(input())+1):     # 탐욕 문제들은 대부분 정렬을 하고 한다
    N = int(input())   # 개수
    times = []
    for i in range(N):
        s, e = map(int, input().split())
        times.append([s, e])

    for i in range(N):  # 뒷 시간을 기준으로 정렬
        for j in range(i, N):
            if times[i][1] > times[j][1]:
                times[i], times[j] = times[j], times[i]

    result = list()
    result.append(times[0])
    visited = [0] * N
    visited[0] = 1
    check()
    print('#{} {}'.format(tc, len(result)))



