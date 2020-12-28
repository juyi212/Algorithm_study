def init():
    st=n//2
    board[st][st]=board[st+1][st+1]=2
    board[st][st+1]=board[st+1][st]=1

def change(c,r,color):
    #돌을 놓았을 때 영향을 미치는 곳의 돌 색깔 바꾸기
    # 8방향을 검사한다.
    # 영역을 벗어나기 전까지 검사하면서, 나랑 같은 돌이 나올때까지 진행하고
    # 같은돌이 나오면, 되돌아오면서 색을 바꾼다.
    board[r][c]=color
    dr=[-1,-1,0,1,1,1,0,-1]
    dc=[]
    for i in range(8):
        nr=r
        nc=c
        while True:
            nr+=dr[i]
            nc+=dc[i]
            if nr<=0 or nr>n or nc<=0 or nc>n or board[nr][nc]==0:
                break
            else:
                if board[nr][nc]==color:
                    while not (nr ==r and nc ==c): # 원래자리로 돌아올때까지
                                nr-=dr[i]
                                nc-=dc[i]
                                board[nr][nc]=color
                    break



t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    board=[[0]*(n+1) for _ in range(n+1)]
    init()

    for i in range(m):
        c,r,color=map(int,input().split())
        change(c,r,color)
