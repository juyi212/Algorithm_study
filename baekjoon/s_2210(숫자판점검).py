# dfs 문제
def dfs(i, j):
    global word
    word.append(matrix[i][j])

    if len(word) == 6:
        check.add(''.join(word))
        return

    for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        nx, ny = i + dx, j+dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny)
            word.pop()


matrix = [list(input().split()) for _ in range(5)]
check = set()
for i in range(5):
    for j in range(5):
        word = []
        dfs(i, j)
print(len(check))