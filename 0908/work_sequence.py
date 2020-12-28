for tc in range(1,11):
    V,E=map(int,input().split()) # 그래프의 정점의 총 수, 간선의 총 수
    matrix=[[] for _ in range(V+1)] #인접리스트 이용
    nodes=list(map(int,input().split()))
    visit=[0]*(V+1)
    count=V
    for i in range(E):
        s=nodes[i*2]
        e=nodes[(i*2)+1]
        matrix[e].append(s) # 4->1 이면 1번이 수행되기 위해서는 4번이 수행되어야 한다./ 전에 수행되어져야하는 노드들을 저장
    result=[]
    while count:
        for i in range(1,len(matrix)):
            if visit[i]==0: #1번 부터 마지막 노드까지 방문여부 체크, 현재 노드가 수행되지 않았다면
                for j in matrix[i]: #선행노드 확인
                    if visit[j]==0: # 선행노드가 수행되지 않았다면 멈춘다.
                        break
                else: # 선행노드가 실행 되었고 현재노드를 수행했다고 바꾸고 결과 출력.
                    visit[i]=1
                    result.append(i)
                    count-=1

    print(f'#{tc}',end=' ')
    print(*result)



'''
10 9
4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9
'''