T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    a=[[0] * N for _ in range(N)]
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    num=1
    cnt=N*N
    x=0
    y=0
    i=0
    while num <= cnt :
        if 0<=x<N and 0<=y<N and not a[x][y]:
            a[x][y] = num
            num += 1
        else:
            x -= dr[i]
            y -= dc[i]
            i = (i + 1) % 4
        x += dr[i]
        y += dc[i]
    print(f'#{test_case}')
    for i in a:
        for j in i:
            print(j,end=' ')
        print()




# a=[9,20,2,18,11,19,1,25,3,21,8,24]

# 저장을하고 출력.

