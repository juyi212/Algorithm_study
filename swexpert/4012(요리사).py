import sys
sys.stdin = open('input17.txt','r')
import itertools

for tc in range(1, int(input())+1):
    N = int(input())    # 식재료 수
    materials = [list(map(int, input().split())) for _ in range(N)]
    count = N//2
    n = range(N)
    # 식자재를 n//2로 나눠야함
    comb = itertools.combinations(n, count)
    min_v = 100000000
    for com in comb:
        sub1 = []
        r1 = 0
        sub2 = []
        r2 = 0
        for j in range(N):
            if j in com:
                sub1.append(j)
            else:
                sub2.append(j)
        for p1 in range(N//2):
            for p2 in range(p1+1, N//2):
                r1 += materials[sub1[p1]][sub1[p2]]
                r1 += materials[sub1[p2]][sub1[p1]]

                r2 += materials[sub2[p1]][sub2[p2]]
                r2 += materials[sub2[p2]][sub2[p1]]

        a = abs(r1-r2)
        if a < min_v:
            min_v = a

    print(f'#{tc} {min_v}')


    #
    #     aa = itertools.combinations(a, 2)
    #     for af in aa:
    #         sum_a += materials[af[0]][af[1]]
    #         sum_a += materials[af[1]][af[0]]
    #
    #     bb = itertools.combinations(b, 2)
    #
    #     for bf in bb:
    #
    #         sum_b += materials[bf[0]][bf[1]]
    #         sum_b += materials[bf[1]][bf[0]]
    #
    #     h = abs(sum_a-sum_b)
    #     if h < min_v:
    #         min_v = h


