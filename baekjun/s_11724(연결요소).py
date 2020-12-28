import sys
from collections import deque

def bfs(v):
    q=deque()
    q.append(v)
    while q:
        vv=q.popleft()
        for j in range(1,n+1):
            if li[vv][j]==1 and not visited[j]:
                visited[j]=True
                q.append(j)
    return

n,m=map(int,sys.stdin.readline().split()) #정점의 개수, 간선의 개수 #연결된 요소를 구해라
li=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for k in range(m):
    s,e=map(int,sys.stdin.readline().split())
    li[s][e]=1
    li[e][s]=1

ans=0
for i in range(1,n+1):
    if not visited[i]:
        visited[i]=True
        bfs(i)
        ans+=1

print(ans)

'''
6 2
3 4
4 2
'''

'''
4 3
4 1
3 1
2 1 


'''

'''
3 2
1 3
2 3
'''
'''
2 1
2 1
'''

'''
3 1

'''