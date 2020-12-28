C,R=map(int,input().split())
K=int(input())

matrix=[[0]*(R) for _ in range(C)]
dr=[0,1,-1,0]
dc=[1,0,0,-1]
i=0
j=0
k=0
cnt=0
if K>R*C:
    print(0)
else:
    while cnt<R*C:
        if 0<=i<C and 0<=j<R and matrix[i][j]==0:
            cnt+=1
            matrix[i][j]=cnt
            if matrix[i][j]==K:
                print('{} {}'.format(i+1,j+1))
                break
        else:
            i=i-dr[k]
            j=j-dc[k]
            k=(k+1)%4
        i=i+dr[k]
        j=j+dc[k]

