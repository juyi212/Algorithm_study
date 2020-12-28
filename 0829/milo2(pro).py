def bfs(s,e):
    q=[] #큐 생성
    q.append((s,e)) #시작점 enq
    visited=[[0]*16 for _ in range(16)] #시작점 처리 표시
    visited[s][e]=1
    while q: #q가 비어있지않으면 반복
        s,e=q.pop(0) #nx,nc칸 방문
        if maze[s][e]==3:
            return 1
        for nx, nc in [(0,1),(1,0),(0,-1),(-1,0)]: # s,e에 인접하고 처리안된 nx,nc를 찾으면
            ns,ne= s+nx,e+nc
            if maze[ns][ne]!=1 and visited[ns][ne]==0:
                q.append((ns,ne))
                visited[ns][ne]=1
    return 0


for _ in range(1,11):
    tc=int(input())
    maze=[list(map(int,input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j]==2:
                print(f'#{tc} {bfs(i,j)}')