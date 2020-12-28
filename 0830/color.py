t=int(input())
for tc in range(1,t+1):
    n=int(input())
    matrix=[[0]*10 for _ in range(10)]
    cnt=0
    for i in range(n):
        r1,c1,r2,c2,color=map(int,input().split())
        for x in range(r1,r2+1):
            for y in range(c1,c2+1):
                matrix[x][y]+=color

    for r in range(10):
        for c in range(10):
            if matrix[r][c]==3:
                cnt+=1
    print(f'#{tc} {cnt}')



