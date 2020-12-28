def dfs(i,j):
    global ans
    dr =[0 ,1 ,0 ,-1]
    dc =[1 ,0 ,-1 ,0]
    for k in range(4):
        nx,ny=i+dr[k],j+dc[k]
        if 0>nx or nx>=N or 0>ny or ny>=N:
            continue
        if 0<=nx<N and 0<=ny<N and rectan[nx][ny]==rectan[i][j]+1:
            ans+=1
            dfs(nx,ny)
    return

t=int(input())
for tc in range(1,t+1):
    N=int(input())
    rectan=[list(map(int,input().split())) for _ in range(N)]
    max_ans=1
    min_v=1000000000000
    li=[]
    for i in range(N):
        for j in range(N):
            ans=1
            dfs(i,j)
            if max_ans<ans: # 클경우
                max_ans=ans
                min_v=rectan[i][j]
            if max_ans==ans: # 같은 경우 작은 방번호를 출력해야함.
                min_v=min(min_v,rectan[i][j])
    print(f'#{tc} {min_v} {max_ans}')
