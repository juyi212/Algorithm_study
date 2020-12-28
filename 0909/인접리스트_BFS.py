#인접리스트
def bfs(v):
    q=[]
    q.append(v)
    visited[v]=1
    print(v, end=' ')
    while q:
        v=q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w]=visited[v]+1
                print(w,end=' ')

G=[[],[2,3],[4,5,6],[],[3,4,5,7]]
bfs(1)
visited=[0]*8