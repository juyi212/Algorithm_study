# 둘레 구하기
def check(i, j):
    ch = 0
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = i+dr, j+dc
        if 0 <= nr <= 100 and 0 <= nc <= 100:
            if matrix[nr][nc] == 1:
                ch += 1
    return ch



matrix = [[0]*101 for _ in range(101)]
# visited = [[False]*100 for _ in range(100)]
for i in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[i][j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if not matrix[i][j]:
            cnt += check(i, j)
print(cnt)