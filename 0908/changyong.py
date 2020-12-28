def check(v): #dfs
    global visit
    visit[v]=1
    for w in range(1,N+1):
        if matrix[v][w]==1 and visit[w]==0:
            visit[w]=1
            check(w)

t=int(input())
for tc in range(1,t+1):
    N, M = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        s,e=map(int,input().split())
        matrix[s][e]=1
        matrix[e][s] = 1
    visit= [0]*(N+1)
    ans=0
    for ww in range(1,N+1):
        if visit[ww]==0: #방문여부로 무리를 확인/ 양문제와 비슷하면서도 약간 다름.
            check(ww)
            ans+=1
    print(f'#{tc} {ans}')


'''
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''