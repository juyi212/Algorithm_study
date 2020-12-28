def dfs(i,j):
    visited[i][j]=1
    global ans
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx=i+dx
        ny=j+dy
        if 0<=nx<16 and 0<=ny<16 and not (nx,ny) in stack and visited[nx][ny]==0 and maze[nx][ny]!=1:
            if maze[nx][ny]==3:
                ans+=1
                return
            stack.append((nx,ny)) #들어갈 길 저장
            dfs(nx,ny)
            stack.pop() # 다시 되돌아갈길 찾기 / pop 위치에 따라 답이 달라지는 경우도 있다.

for _ in range(1,11):
    tc=int(input())
    maze=[list(map(int,input())) for _ in range(16)]
    visited=[[0]*16 for _ in range(16)]
    stack=[]
    ans=0
    for i in range(16):
        for j in range(16):
            if maze[i][j]==2:
                stack=[(i,j)]
                if dfs(i,j):
                    print(f'#{tc} {ans}')
                else:
                    print(f'#{tc} {ans}')
                