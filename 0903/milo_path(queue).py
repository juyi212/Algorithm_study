def milo(i,j):
    global num
    q=[]
    q.append((i,j,0))
    visited[i][j]=1
    while q:
        s,e,l=q.pop(0)
        for dr,dc in [(0,-1),(-1,0),(0,1),(1,0)]:
            nr,nc=s+dr,e+dc
            if 0<=nr<n and 0<=nc<n and matrix[nr][nc]!=1 and visited[nr][nc]==0:
                if matrix[nr][nc] == 3:
                    return l
                q.append((nr,nc,l+1))
                visited[nr][nc]=1
    return 0


t=int(input())
for tc in range(1,t+1):
    n=int(input())
    matrix=[list(map(int,input().rstrip())) for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    num=0
    for i in range(n-1,0,-1):
        for j in range(n):
            if matrix[i][j]==2:
                print(f'#{tc} {milo(i,j)}')