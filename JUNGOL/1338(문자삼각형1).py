n = int(input())
li = [[0]*n for _ in range(n)]

num = 64
i = 0
while i != n:
    j = i
    k = n - 1
    while j != n:
        if num < 90:
            num += 1
            li[j][k] = chr(num)
        else:
            num = 65
            li[j][k] = chr(num)
        j += 1
        k -= 1
    i += 1


for i in range(n):
    for j in range(n):
        if li[i][j] == 0:
            print(' ', end =' ')
        else:
            print(li[i][j], end = ' ')
    print()