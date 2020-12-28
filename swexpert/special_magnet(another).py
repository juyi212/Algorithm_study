def check(n, k):
    tf = [False] * 4
    tf[n-1] = True

    for i in range(n-1, 3):
        if magnet[i][2] != magnet[i+1][6]:
            tf[i+1] = True
        else:
            break

    for i in range(n-1, 0, -1):
        if magnet[i-1][2] != magnet[i][6]:
            tf[i-1] = True
        else:
            break
    # 방향 설정 넣어줘야함
    d = [0] * 4
    for i in range(4):
        if (i-n-1) % 2 == 0:
            d[i] = k
        else:
            d[i] = -k

    for i in range(4):
        if tf[i]:
            if d[i] == 1:
                a = magnet[i].pop()
                magnet[i].insert(0, a)
            else:
                a = magnet[i].pop(0)
                magnet[i].append(a)

t = int(input())
for tc in range(1, t+1):
    k = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]    # 마그넷
    for i in range(k):
        n, d = map(int, input().split())    # 번호와 방향
        # 2, 6번 idx 확인 해야함
        check(n, d)

    ans = 0
    for i in range(4):
        if magnet[i][0] == 1:
            ans += 2**i
    print(ans)

'''
1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1
'''