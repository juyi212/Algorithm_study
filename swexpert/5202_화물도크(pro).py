# 종료시간이 가장 빠른 am 선택 이건 무조건 답
# a1 의 종료시간에 맞거나 이상인 친구들 중에서 해를 구함

import sys
sys.stdin = open('input9.txt', 'r')

for tc in range(1, int(input())+1):     # 탐욕 문제들은 대부분 정렬을 하고 한다
    N = int(input())   # 개수
    jobs = [list(map(int, input().split())) for _ in range(N)]

    # 종료시간순으로 정렬
    jobs.sort(key = lambda x: x[1])

    ans = 1
    finish = jobs[0][1]

    for i in range(1, N):
        if jobs[i][0] >= finish:
            ans += 1
            finish = jobs[i][1]

    print(ans)