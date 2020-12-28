t=int(input())
for tc in range(1,t+1):
    E,N=map(int,input().split()) #E는 간선, 노드번호는 1,E+1까지 존재
    L=[0]*(E+2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)
    arr=list(map(int,input().split()))
    for i in range(0,E*2,2):
        p,c=arr[i],arr[i+1]


        if L[p]:R[p]=c
        else:
            L[p]=c
        P[c]=p

    def traverse(v):
        if v==0:
            return 0
        l=traverse(L[v])
        r=traverse(R[v])
        return l+r+1 # 자기자신도 더해야함
    #traverse(L[v])+traverse(R[v])+1 return 도 가능
    print(traverse(N))