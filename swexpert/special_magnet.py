t = int(input())
for tc in range(1, t+1):
    k = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]    # 마그넷

    for i in range(k):
        n, d = map(int, input().split())    # 번호와 방향
        # 2, 6번 idx 확인 해야함
        tf = [False] * 4
        gogo = list()
        gogo.append([n, d])

        while gogo:
            n, d = gogo.pop()
            if n == 1:
                tf[0] = True
                if magnet[0][2] != magnet[1][-2] and not tf[1]:
                    gogo.append([2, -d])
                if d == 1:
                    a = magnet[0].pop()
                    magnet[0].insert(0, a)
                elif d == -1:
                    a = magnet[0].pop(0)
                    magnet[0].append(a)
            elif n == 2:
                tf[1] = True
                if magnet[0][2] != magnet[1][-2] and not tf[0]:
                    gogo.append([1, -d])
                if magnet[1][2] != magnet[2][-2] and not tf[2]:
                    gogo.append([3, -d])
                if d == 1:
                    a = magnet[1].pop()
                    magnet[1].insert(0, a)
                elif d == -1:
                    a = magnet[1].pop(0)
                    magnet[1].append(a)
            elif n == 3:
                tf[2] = True
                if magnet[1][2] != magnet[2][-2] and not tf[1]:
                    gogo.append([2, -d])
                if magnet[2][2] != magnet[3][-2] and not tf[3]:
                    gogo.append([4, -d])
                if d == 1:
                    a = magnet[2].pop()
                    magnet[2].insert(0, a)
                elif d == -1:
                    a = magnet[2].pop(0)
                    magnet[2].append(a)
            elif n == 4:
                tf[3] = True
                if magnet[2][2] != magnet[3][-2] and not tf[2]:
                    gogo.append([3, -d])
                if d == 1:
                    a = magnet[3].pop()
                    magnet[3].insert(0, a)
                elif d == -1:
                    a = magnet[3].pop(0)
                    magnet[3].append(a)


    ans = 0
    for m in range(4):
        if magnet[m][0] == 1:
            ans += 2 ** m
    print(f'#{tc} {ans}')
