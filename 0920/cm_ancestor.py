t=int(input())

def inorder(n):
    if n:
        check[tree[n][2]]+=1
        if check[tree[n][2]]==2:
            return
        inorder(tree[n][2])

def node_check(n):
    global ans
    if n:
        ans+=1
        node_check(tree[n][0])
        node_check(tree[n][1])


for tc in range(1,t+1):
    V,E,N1,N2=map(int,input().split())
    nodes=list(map(int,input().split()))
    tree=[[0]*3 for _ in range(V+1)]
    for i in range(E):
        p,c=nodes[2*i],nodes[2*i+1]
        if tree[p][0]==0:
            tree[p][0]=c
        elif tree[p][0]!=0:
            tree[p][1]=c
        tree[c][2] = p #부모 체크

    check=[0]*(V+1)
    ans=0
    inorder(N1)
    inorder(N2)
    print(check.index(2))
    node_check(check.index(2))
    print(ans)
