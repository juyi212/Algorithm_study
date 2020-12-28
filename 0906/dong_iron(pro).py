def f1(n,k,percent): #n번 사람이 맡을 일의 번호를 결정
    global max_v
    if n==k: # i번 사람이 p[i]일을 맡았을 때의 확률
        if percent>max_v:
            max_v=percent
    else:
        for i in range(k):
            if u[i]==0:#i번 일을 맡은 사람이 없으면
                u[i]=1 # i번 일을 배정
                p[n]=i #n번 사람이 i번 일을 맡음
                if max_v<percent*matrix[n][i]:
                    f1(n+1,k,percent*matrix[n][i]) # n+1번 사람이 맡을 일을 결정,n번 사람이 i번 일을 맡을 때의 성공확률을 곱함
                u[i]=0 #i번 일을 다른 사람이 맡을 수 있도록 함.
    return

def f3(n,k,s): #자리를 바꿔서 일의 여부를 넣어줌
    global max_v
    if n==k: # i번 사람이 p[i]일을 맡았을 때의 확률
        if max_v<s*100:
            max_v=s*100
    elif max_v>=s*100:
        return
    else:
        for i in range(n,k):
            p[n],p[i]=p[i],p[n] # 자기 자신을 포함해 오른쪽과 자리를 바꿈
            f3(n+1,k,s*matrix[n][p[n]])
            p[n],p[i]=p[i],p[n] #다시 원상복구


# 순열과 관련이 있다.
t=int(input())
for tc in range(1,t+1):
    N=int(input())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    #p=[0]*N #p[n] n번 사람이 맡은 일의 번호 f1
    p=[ i for i in range(N)]
    u=[0]*N #u[i] i번 일의 배정 여부
    max_v=0.0000000001
    for i in range(N):
        for j in range(N):
            matrix[i][j]=matrix[i][j]/100
    # f1(0,N,1)
    f3(0,N,1)
    print(f'#{tc} {max_v:.6f}')
