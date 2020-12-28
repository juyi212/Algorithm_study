import sys
sys.setrecursionlimit(100000)

def check(i,j):
    dr=[-1,-1,0,1,1,1,0,-1]
    dc=[0,1,1,1,0,-1,-1,-1]
    for k in range(8):
        nr=i+dr[k]
        nc=j+dc[k]
        if 0<=nr<h and 0<=nc<w and matrix[nr][nc]=='1':
            matrix[nr][nc]='0'
            check(nr,nc)

while True:
    w,h =map(int,input().split())
    matrix=[list(input().split()) for _ in range(h)]
    if w==0 and h==0:
        break
    ans=0
    visited=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if matrix[i][j]=='1':
                ans+=1
                check(i,j)
    print(ans)