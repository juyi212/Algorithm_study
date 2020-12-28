t=int(input())
for tc in range(1,t+1):
    n=int(input())
    matrix=[[0]*n for _ in range(n)]
    dr=[0,1,0,-1,0]
    dc=[1,0,-1,0,1]
    num=1
    cnt=n*n
    i=0
    j=0
    k=0
    while num<=cnt:
        if 0<=i<n and 0<=j<n and not matrix[i][j]:
            matrix[i][j]=num
            num+=1
        else:
            i-=dr[k]
            j-=dc[k]
            k=(k+1)%4
        i+=dr[k]
        j+=dc[k]
    print(matrix)
