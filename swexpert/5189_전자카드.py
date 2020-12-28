# 완전 검색
import sys
sys.stdin = open('input8.txt', 'r')


def check(n, total):
    global min_p
    if len(visited) == N:
        total += matrix[n][0]
        if min_p > total:
            min_p = total
    else:
        for i in range(N):
            if i != n and i not in visited:
                visited.append(i)
                check(i, total + matrix[n][i])
                visited.pop()


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]
    min_p = 10000000
    check(0, 0)
    print('#{} {}'.format(tc, min_p))