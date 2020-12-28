import sys
from collections import deque

def bfs(r,c,fuel): #짧은 거리 찾는
    q=deque()
    s=deque()
    q.append((r,c))
    q1=[]
    visited=[]
    visited.append((r,c))
    while True:
        while q:
            r,c=q.popleft()
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<N and 0<=nc<N and matrix[nr][nc]!=1 and not (nr,nc) in visited:
                    visited.append((nr,nc))
                    if cus.get((nr,nc)) is not None:
                        q1.append((nr, nc))
                    else:
                        s.append((nr,nc))
        fuel-=1
        if fuel<0:
            return -1
        elif q1:
            if len(q1)>0:
                q1.sort()
            return q1[0][0],q1[0][1],fuel
        else:
            q=s
            s=deque()

def bfs_a(r,c,x,y,fuel): #이동 연료 찾는거
    q=deque()
    q.append((r,c,0))
    visited=[]
    visited.append((r,c))
    while q:
        r,c,cnt=q.popleft()
        if fuel<0:
            return -1
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and matrix[nr][nc]!=1 and not (nr,nc) in visited:
                visited.append((nr,nc))
                if nr==x and nc ==y:
                    return cnt+1
                q.append((nr,nc,cnt+1))
    return -1


N,M,fuel=map(int,sys.stdin.readline().split()) #matrix 크기, 승객 수, 연료
matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
r,c=map(int,sys.stdin.readline().split()) # 처음 택시 출발공간
r-=1
c-=1

cus={}
for _ in range(M):
    point=list(map(int,sys.stdin.readline().split()))
    cus[(point[0]-1,point[1]-1)]=[point[2]-1,point[3]-1]

while True:
    nn,cc,fuel=bfs(r,c,fuel)
    if fuel<0:
        print(-1)
        break
    x,y=cus[(nn,cc)]
    if x==nn and y==cc:
        value=0
    else:
        value=bfs_a(nn,cc,x,y,fuel)

    if value>fuel:
        print(-1)
        break
    else:
        fuel+=value
        del cus[(nn,cc)]
        if not cus:
            print(fuel)
            break
        r=x
        c=y

