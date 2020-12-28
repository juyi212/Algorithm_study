def check(n):
    if n>1:
        visited[tree[n][2]]+=1
        if visited[tree[n][2]]==2: #숫자가 작다고 부모노드가 아닐 수 있음.
            return
        check(tree[n][2])

def node_check(v):
    global ans
    if v:
        ans+=1
        node_check(tree[v][0])
        node_check(tree[v][1])

t=int(input())
for tc in range(1,t+1):
    V,E,N1,N2=map(int,input().split())
    nodes=list(map(int,input().split()))
    tree=[[0]*3 for _ in range(V+1)]
    visited=[0]*(V+1)
    ans=0
    for i in range(E):
        p,c=nodes[i*2],nodes[i*2+1]
        if tree[p][0]==0:
            tree[p][0]=c
        else:
            tree[p][1]=c
        tree[c][2]=p
    check(N1)
    check(N2)
    print(f'#{tc}',end=' ')
    node_check(visited.index(2))
    print(f'{visited.index(2)} {ans}')