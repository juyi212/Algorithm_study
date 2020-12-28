def dfs(idx,sum_m):
    global min_c
    if idx==n: #모든 행을 다 돌면 return
        if sum_m<= min_c:
            min_c=sum_m
            return


    for w in range(n):
        if visited[w]==0:
            visited[w]=1 #세로줄 다시 방문 하지 못하게
            if min_c>sum_m+cards[idx][w]: # 최소값보다 더해지는 값들이 커지면 할 필요가 없음
                dfs(idx+1,sum_m+cards[idx][w])
            visited[w]=0

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    cards=[list(map(int,input().split())) for _ in range(n)]
    min_c=1000000000
    visited=[0]*n
    dfs(0,0)#행 기준
    print(f'#{tc} {min_c}')

'''
1
3
2 1 2
5 8 5
7 2 2
'''
#
# if cities_c[node][start_node] != 0:
#     s += cities_c[node][start_node]