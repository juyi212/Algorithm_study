def check(n, s):
    global minv
    if n > 12: # 12달 이상은 없으니깐 !
        if s < minv:
            minv = s
    else:
        check(n+1, s+ month[n]*d)
        check(n + 1, s+m)
        check(n + 3, s+three_m)


# 완전 탐색
for tc in range(1, int(input())+1):
    d, m, three_m, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    minv = y
    check(1, 0)
    print(f'#{tc} {minv}')

'''
10      
10 40 100 300   
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300   
0 0 0 0 0 0 0 0 6 2 7 8
'''