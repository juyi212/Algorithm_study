# 비선형구조인 그래프 구조(트리도)는 그래프로 표현된 모든 자료를 빠짐 없이
#검색하는 것이 중요함. -> 표현: 인접행렬,인접리스트,간선배열 / 순회: dfs,bfs
# stack, 재귀 이용 ! 가장 최근의 갈림길로 되돌아가기때문

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    #방문 체크
    visited[v]=1
    print(v, end = " ")
    # v의 인접한 정점중에서 방문 안한 정점을 재귀호출
    for w in range(1,N+1):
        if G[v][w] == 1 and visited[w]==0:
            dfs(w)

# 정점, 간선
N,E =map(int,input().split())
# 간선들
temp=list(map(int,input().split()))
# 인접행렬
G=[[0]*(N+1) for _ in range(N+1)]
# 방문체크
visited=[0]*(N+1)
# 간선들을 인접행렬에 입력저장
for i in range(E):
    s,e= temp[2*i],temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1
dfs(2)
print(visited)

