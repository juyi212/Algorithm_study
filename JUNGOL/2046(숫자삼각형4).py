n, m = map(int, input().split())

if m == 1:
    for i in range(n):
        for j in range(n):
            print(i+1, end = ' ')
        print()
elif m == 2:
    li = list(range(1, n+1))
    for i in range(n):
        if i%2 == 0:
            print(*li)
        else:
            print(*li[::-1])
else:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end = ' ')
        print()