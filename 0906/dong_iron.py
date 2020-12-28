#순열을 만들줄 알아야한다.
def check(idx,percent):
    global max_p
    if idx==N:
        if percent>max_p:
            max_p=percent
            return

    for w in range(N):
        if visit[w]==0:
            visit[w]=1
            if max_p<percent*(matrix[idx][w]): #곱해진 것들이 max_p보다 크면 진행 아니면 x 가지치기
                check(idx+1,percent*(matrix[idx][w]))
            visit[w]=0


t=int(input())
for tc in range(1,t+1):
    N=int(input())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    for i in range(N): #미리 100으로 나눠줌
        for j in range(N):
            matrix[i][j]=(matrix[i][j])/100
    max_p=0.000001
    visit=[0]*N #방문 여부 체크
    check(0,1) #percent 이기때문

    print(f'#{tc} {max_p*100:.6f}')
