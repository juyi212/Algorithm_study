for tc in range(1,11):
    data_l,start_n= map(int,input().split())
    nodes=list(map(int,input().split()))
    matrix=[[0]*101 for _ in range(101)]
    for i in range(0,data_l,2):
        matrix[nodes[i]][nodes[i+1]]=1
    visit=[0]*101
    q=[start_n]
    visit[start_n]=1

    while q:
        v=q.pop(0)
        for w in range(1,101):
            if matrix[v][w] and not visit[w]:
                visit[w]=visit[v]+1 #시작점에서 각 정점까지 거리가 적혀짐
                q.append(w)

    ans = 1
    for i in range(2,100):
        if visit[ans] <= visit[i]: # 같을 경우에도 인덱스가 높은 것으로 바꿔준다.
            ans=i
    print(ans)