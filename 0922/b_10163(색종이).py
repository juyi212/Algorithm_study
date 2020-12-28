n=int(input())

matrix=[[0]*101 for _ in range(101)]
for k in range(1,n+1):
    x1,y1,w,h=map(int,input().split())
    for i in range(x1,x1+w):
        for j in range(y1,y1+h):
            matrix[i][j]=k

for k in range(1,n+1):
    cnt=0
    for i in matrix:
        for j in i:
            if j==k:
                cnt+=1
    print(cnt)

