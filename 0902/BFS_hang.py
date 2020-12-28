def bfs(v):
    #큐, 방문

    Q=[]
    visit=[0]*V+1
    #enQ(v), visit(v)
    Q.append(v)
    visit[v]=1
    # 큐가 비어있지 않은 동안
    print(v, end=' ')
    while Q:
        #v=deQ()
        v=Q.pop(0)
        #v의 인접한 정점(w), 방문 안한 정점이면
        for w in range(1,V+1):
            if G[v][w] ==1 and visit==0:
                Q.append(w)
                visit[w]=1
                print(v,end=' ')
            #enQ(w),방문처리(w)

V,E=map(int,input().split())
temp=list(map(int,input().split()))
# 인접행렬 초기화
G=[[0*V+1 for _ in range(V+1)]]
# 인정행렬 저장
for i in range(E):
    s,e=temp[2*i], temp[2*i+1]
    G[s][e]=G[e][s]=1
