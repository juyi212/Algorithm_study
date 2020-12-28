for tc in range(1,int(input())+1):
    V,E=map(int,input().split())

    G=[[0]*(V+1) for _ in range(V+1)]
    # G=[[] for _ in range(V+1)] #인접리스트로 했을 떼
    for _ in range(E):
        u,v=map(int,input().split())
        G[u][v]=G[v][u]=1
        #G[u].append(v)
        # G[v].append(u)
    s,e=map(int,input().split())
    visit=[0]*(V+1)
    Q=[s]
    visit[s]=1 #출발점 방문하고 큐에 삽입

    while Q: # 빈큐가 아닐 동안
        v=Q.pop(0)

        # v==e: break
        for w in range(1,V+1): # in G[v]
            if G[v][w] and not visit[w]:
                visit[w]=visit[v]+1 # 거리 계산
                if w==e:
                    Q.clear()
                    break
                Q.append(w)
    print(visit)
    print(visit[e]-1) #처음 출발 한 시점을 1로 뒀기때문에 1을빼준다.
