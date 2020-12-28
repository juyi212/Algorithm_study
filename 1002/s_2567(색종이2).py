import collections

t=int(input())
matrix=[[0]*101 for _ in range(101)]
visited=[[0]*101 for _ in range(101)]

def bfs(r,c):
    ans=0
    q=collections.deque()
    visited[r][c] = 1
    q.append([r,c])
    while q:
        r,c = q.popleft()
        for nx,ny in [(-1,0),(1,0),(0,1),(0,-1)]:
            nr,nc=r+nx,c+ny
            if 0<=nr<=101 and 0<=nc<=101 and visited[nr][nc]==0:
                if matrix[nr][nc]:
                    q.append([nr,nc])
                    visited[nr][nc]=1
                else: #색종이의 겉표면을 count 해야한다.
                    ans+=1
    return ans

def first(x,y):
    for i in range(x,x+10):
        for j in range(y,y+10):
            matrix[i][j]=1

for tc in range(t):
    x,y=map(int,input().split())
    first(x,y)


result=0
for i in range(101):
    for j in range(101):
        if matrix[i][j] and visited[i][j]==0:
            result+=bfs(i,j)

print(result)
