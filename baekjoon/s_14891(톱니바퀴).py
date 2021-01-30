import sys
magnet = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(4)]

k = int(input())
for _ in range(k):
    n, d = map(int, sys.stdin.readline().split())
    q = [(n, d)]
    check = [False] * 4
    while q:
        n, d = q.pop()
        if n == 1:
            check[0] = True
            if magnet[0][2] != magnet[1][6] and not check[1]:
                q.append((2, -d))
            if d == 1:
                a = magnet[0].pop()
                magnet[0].insert(0, a)
            elif d == -1:
                a = magnet[0].pop(0)
                magnet[0].append(a)
        elif n == 2:
            check[1] = True
            if magnet[0][2] != magnet[1][6] and not check[0]:
                q.append((1, -d))
            if magnet[1][2] != magnet[2][6] and not check[2]:
                q.append((3, -d))
            if d == 1:
                a = magnet[1].pop()
                magnet[1].insert(0, a)
            elif d == -1:
                a = magnet[1].pop(0)
                magnet[1].append(a)
        elif n == 3:
            check[2] = True
            if magnet[1][2] != magnet[2][6] and not check[1]:
                q.append((2, -d))
            if magnet[2][2] != magnet[3][6] and not check[3]:
                q.append((4, -d))
            if d == 1:
                a = magnet[2].pop()
                magnet[2].insert(0, a)
            elif d == -1:
                a = magnet[2].pop(0)
                magnet[2].append(a)
        elif n == 4:
            check[3] = True
            if magnet[2][2] != magnet[3][6] and not check[2]:
                q.append((3, -d))
            if d == 1:
                a = magnet[3].pop()
                magnet[3].insert(0, a)
            elif d == -1:
                a = magnet[3].pop(0)
                magnet[3].append(a)

ans = 0
for i in range(4):
    if magnet[i][0] == 1:
        ans += 2**i
print(ans)