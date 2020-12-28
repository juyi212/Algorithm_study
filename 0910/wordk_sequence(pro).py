#선행작업이 만족되어야지 노드를 돌 수 있다.
t=10
for tc in range(1,t+1):
    V,E=map(int,input().split())
    edges=list(map(int,input().split()))
    adj=[[0]*(V+1) for _ in range(V+1)]

    #선행 작업이 없는 것을 먼저 찾아줘야한다.
    prev_arr=[[0]*(V+1) for _ in range(V+1)]
    #작업 순서를 저장할 리스트
    order_list=[]
    for i in range(0,len(edges),2):
        adj[edges[i]][edges[i+1]]=1
        prev_arr[edges[i+1]][edges[i]] = 1 #선행작업을 저장할 배열

    for i in range(1,len(prev_arr)):
        #선행작없이 없음,
        if prev_arr[i].count(1)==0:
            order_list.append(i)
        #노드들을 순회하면서, orderlist에 넣을지를 결정
        #선행 작업 목록 확인해서, 선행작없들이 모두 orderlist에 들어가 있으면, 선행작업이 완료된 상황>> order list에 넣음
        #orderlist에 모든 노드들이 들어갈 때 까지 반복

    while len(order_list)<V:
        for i in range(1,V+1):
            if i not in order_list: #i번째 노드 작업하지 않음
                #i번 노드의 선행작업이 모두 이루어졌는지 확인
                #선행 작업 prearr 확인
                for j in range(1,V+1):
                    if prev_arr[i][j]==1 and j not in order_list:
                        #i는 작업하면 안됨
                        break
                else: #break가 안걸리면, 선행작업이 완료된 상황
                    order_list.append(i)
    print(f'#{tc}',end=' ')
    print(*order_list)

