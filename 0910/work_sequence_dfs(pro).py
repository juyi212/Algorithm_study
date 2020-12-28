#DFS
#아까전 반복문은 선행작업 먼저 처리
# 이번에는 깊이 우선으로 진행하면서, 후행작업먼저 stack에 넣고
def dfs(v):
    visited[v]=1
    #모든 후행작업 확인 후 , 실행하지 않은 후행작업 있으면 후행작업부터 탐색
    for i in range(1,V+1):
        if adj[v][i]==1 and not visited[i]:
            dfs(i)
    #for 문이 끝나면, 후행작업을 모두 마친 상태
    # 후행작없이 없으면, 자기 자신을 stack에 넣는다.
    stack.append(v)

t=10
for tc in range(1,t+1):
    V,E=map(int,input().split())
    edges=list(map(int,input().split()))
    adj=[[0]*(V+1) for _ in range(V+1)]

    #선행 작업이 없는 것을 먼저 찾아줘야한다.
    prev_arr=[[0]*(V+1) for _ in range(V+1)]

    stack=list() #작업순서 후행으로 먼저 push 할 stack
    visited=[0]*(V+1) # 노드 방문 여부 체크
    for i in range(0,len(edges),2):
        f,t=edges[i],edges[i+1] #from/to
        adj[f][t]=1 #각 행의 인덱스에 해당하는 노드의 후행작업 노드들 표시(인접행렬)
        prev_arr[t][f]=1 #선행작업

    #선행작업이 없는 위치에서 깊이 우선 탐색 실행
    for i in range(1,V+1):
        if prev_arr[i].count(1)==0: #선행작업 없음
            #깊이 우선 탐색 실행
            dfs(i)
    print(f'#{tc}',end=' ')
    print(*stack[::-1]) #후행작업이 나중에 빠져나온다는 것을 이용


