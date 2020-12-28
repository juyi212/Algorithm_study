
# 행렬 만들어서 풀기

def dfs(S):# 들어온 node에서의 모든 노드 탐색
    global ans
    visited[S]=1
    print(S,end='')
    for w in range(1,V+1):
        if checked[S][w]==1 and visited[w]==0:
            if w==G:
                ans=1
            dfs(w)

t=int(input())
for tc in range(1,t+1):
    V,E=map(int,input().split())
    checked=[[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)
    for i in range(E):
        s,e=map(int,input().split())
        checked[s][e]=1
    S,G = map(int,input().split())
    ans=0
    dfs(S)
    print(f'#{tc} {ans}')
