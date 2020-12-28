n, k = map(int, input().split())

cnt = 0
check = False
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
            check = True
            break

if not check:
    print(0)