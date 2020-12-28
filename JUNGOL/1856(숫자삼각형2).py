n, m = map(int, input().split())

matrix = [[0]*m for _ in range(n)]
num = 0
for i in range(n):
    for j in range(m):
        num += 1
        matrix[i][j] = num

for i in range(n):
    if i%2 == 1:
        for k in range(m-1, -1, -1):
            print(matrix[i][k], end =' ')
        print()
    else:
        for j in range(m):
            print(matrix[i][j], end =' ')
        print()

