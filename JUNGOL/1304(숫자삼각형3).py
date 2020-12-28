n = int(input())

num = 0
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        num += 1
        matrix[j][i] = num

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()