t=int(input())

def tree(n):
    global ans
    ans+=1
    if n:
        if matrix[n][0]!=0:
            tree(matrix[n][0])
        if matrix[n][1]!=0:
            tree(matrix[n][1])
        return

for tc in range(1,t+1):
    E,N=map(int,input().split()) # E 간선의 개수, N 찾을 노드
    V=E+1 #노드의 개수
    matrix=[[0]*2 for _ in range(V+1)]
    nodes=list(map(int,input().split()))
    for i in range(E):
        p,c=nodes[2*i],nodes[(2*i)+1]
        if matrix[p][0]==0:
            matrix[p][0]=c
        else:
            matrix[p][1]=c

    ans=0
    tree(N)
    print(ans)
