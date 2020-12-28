t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    flies=[list(map(int,input().split())) for _ in range(n)]
    max_f=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum=0
            for x in range(i,i+m):
                for y in range(j,j+m):
                    sum+=flies[x][y]
            if max_f<sum:
                max_f=sum
    print(f'{tc} {max_f}')
