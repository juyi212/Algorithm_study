def dfs(x,y,cnt,sentence):
    sentence+=matrix[x][y]
    if cnt==6:
        result.add(sentence)
        return
    for dx, dy in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, cnt + 1, sentence)

t=int(input())
for tc in range(1,t+1):
    matrix=[list(input().split()) for _ in range(4)]
    result=set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,'')
    print(f'#{tc} {len(result)}')