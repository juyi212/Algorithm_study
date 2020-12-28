
n = int(input())
li = [[0]*n for _ in range(n)]
num = 64

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if num < 90:
            num += 1
            li[j][i] = chr(num)
        else:
            num = 65
            li[j][i] = chr(num)

for i in range(n):
    for j in range(n):
        print(li[i][j], end = ' ')
    print()