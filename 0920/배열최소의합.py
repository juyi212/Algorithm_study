t=int(input())

def dfs(idx,s):
    global min_c

    if idx==n: #return 조건
        if min_c> s:
            min_c=s

    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            if min_c>s+li[idx][i]: #가지치기
                dfs(idx+1,s+li[idx][i])
            visited[i]=0

for tc in range(1,t+1):
    n=int(input())
    li=[list(map(int,input().split())) for _ in range(n)]
    visited=[0]*n
    min_c=1000000000
    dfs(0,0)
    print(min_c)