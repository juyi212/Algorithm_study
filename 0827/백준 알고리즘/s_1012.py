import sys
sys.setrecursionlimit(50000)

def dfs(i,j):
    checked[i][j]=1
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for k in range(4):
        dx=i+dr[k]
        dy=j+dc[k]
        if 0>dx or m<=dx or 0>dy or dy>=n:
            continue
        if baba[dx][dy]==1 and not checked[dx][dy]:
            dfs(dx,dy)

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    baba=[[0]*n for _ in range(m)]
    checked=[[0]*n for _ in range(m)]
    num=0
    for i in range(k):
        r,c=map(int,input().split())
        baba[r][c]=1

    for i in range(m):
        for j in range(n):
            if baba[i][j]==1 and not checked[i][j]:
                dfs(i,j)
                num += 1
    print(num)