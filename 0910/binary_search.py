def maketree(i): #4 2 6 1 3 5
    global count
    if i<=N: #중위
        maketree(i*2) #왼 맨밑부터
        matrix[i]=count
        count+=1
        maketree(i*2+1)

t=int(input())
for tc in range(1,t+1):
    N=int(input())
    tree=[i for i in range(1,N+1)]
    matrix=[0]*(N+1)
    count=1
    #트리를 만들어준다 제일 낮은 순서부터
    maketree(1)
    print(matrix)
    print(f'#{tc} {matrix[1]} {matrix[N//2]}')
