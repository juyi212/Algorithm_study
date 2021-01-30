def bfs(s1,s2,e1,e2):
    q=[]
    visited[s1][s2]=True
    q.append((s1,s2,0))
    while q:
        s1,s2,tmp=q.pop(0)
        if s1==e1 and s2==e2:
            return tmp
        for dx,dy in [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]:
            nx,ny=s1+dx,s2+dy

            if 0<=nx<l and 0<=ny<l and not visited[nx][ny]:
                # matrix[nx][ny]+=matrix[s1][s2]
                q.append((nx,ny,tmp+1))
                visited[nx][ny]=True


#   저장해 나가면서 푸는 방법도 있음.
t=int(input())
for tc in range(t):
    l=int(input()) #한 변의 길이
    s1,s2=map(int,input().split())
    e1,e2=map(int,input().split())
    visited = [[False] * l for _ in range(l)]
    print(bfs(s1,s2,e1,e2))
