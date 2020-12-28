def check(node):
    global ans
    ans += 1
    if node:
        if tree[node][0] != 0:
            check(tree[node][0])
        if tree[node][1] != 0:
            check(tree[node][1])
        return

t=int(input())
for tc in range(1,t+1):
    E,N=map(int,input().split()) #E는 간선, 노드번호는 1,E+1까지 존재
    numbers=list(map(int,input().split()))
    tree=[[0]*2 for _ in range(E+2)]
    for i in range(E):
        p,c=numbers[i*2],numbers[i*2+1]
        if tree[p][0]==0: #왼
            tree[p][0]=c
        else:#오
            tree[p][1]=c
    ans=0
    check(N)
    print(f'#{tc} {ans}')