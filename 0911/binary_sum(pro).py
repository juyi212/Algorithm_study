def dfs(v): #어디에서 어떤 값을 리턴해야하나를 생각해봐야한다.

    if v>N: return 0
    l=dfs(v*2)
    r=dfs(v*2+1)
    matrix[v]+=l+r

    return matrix[v]


t=int(input())
for tc in range(1,t+1):
    N,M,L=map(int,input().split())
    matrix=[0]*(N+1)
    for _ in range(M):
        num,val=map(int,input().split())
        matrix[num]=val
    #트리를 만들어준다 제일 낮은 순서부터
    dfs(1)
    print(matrix)