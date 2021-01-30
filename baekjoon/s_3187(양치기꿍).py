def bfs(x,y):
    k_cnt = 0
    v_cnt = 0
    q=[]
    q.append((x,y))
    while q:
        x,y=q.pop(0)
        if field[x][y] == 'k':
            k_cnt += 1
        if field[x][y] == 'v':
            v_cnt += 1
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<R and 0<=ny<C and field[nx][ny] != '#' and visited[nx][ny]==False:
                visited[nx][ny] = True
                q.append((nx, ny))

    return k_cnt,v_cnt

R,C=map(int,input().split())
field=[list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
r_cnt=0
c_cnt=0
for i in range(R):
    for j in range(C):
        if field[i][j]!='#' and visited[i][j]==False:
            visited[i][j]=True
            kk,vv=bfs(i,j)
            if vv>=kk:
                c_cnt+=vv
            else:
                r_cnt+=kk
print(r_cnt,c_cnt)


