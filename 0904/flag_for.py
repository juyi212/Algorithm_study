t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split()) # n 행 , m 열
    colors=[list(input().rstrip()) for _ in range(n)]
    print(colors)
    W=[m]*n
    B=[m]*n
    R=[m]*n

    for i in range(n): # 각 행마다 바꿔줘야하는 color의 수
        for j in range(m):
            if colors[i][j]=='W':
                W[i]-=1
            elif colors[i][j]=='B':
                B[i]-=1
            elif colors[i][j]=='R':
                R[i]-=1

    for i in range(n-1):
        W[i+1]+=W[i]
        B[i + 1] += B[i]
        R[i + 1] += R[i]
    print(W)
    print(B)
    print(R)


    for w in range(n-2):
        for b in range(w+1,n-1):
            for r in range(b+1,n):



'''
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
'''