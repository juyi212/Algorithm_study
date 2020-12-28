from collections import deque

def bfs(f,e):
    count=0
    visited=[False]*(n+1) #boolean 으로 하면 속도가 빨라짐
    q=deque([[f,count]])
    while q:
        v=q.popleft()
        f=v[0]
        cnt=v[1]
        if f==e:
            return cnt
        for i in re[f]:
            if not(visited[i]):
                visited[i]=True
                q.append([i,cnt+1])
    return -1


n=int(input()) #사람수
f,e=map(int,input().split()) # 찾을 관계
m=int(input()) #부모 자식들 간의 관계 개수

re=[[] for _ in range(n+1)]

for _ in range(m):
    p,c=map(int,input().split())
    re[p].append(c)
    re[c].append(p)

print(bfs(f,e))

