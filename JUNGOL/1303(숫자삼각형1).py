n, m = map(int, input().split())


num = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        num += 1
        print(num, end = ' ')
    print()