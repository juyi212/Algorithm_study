T=int(input())
for _ in range(T):
    r,c = map(int,input().split())
    sheep=[list(input().rstrip()) for _ in range(r)]
    check=[[0]*c for _ in range(r)]
    num=1
    cnt=r*c
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dx=0
    dy=0
    for x in range(r):
        for y in range(c):
            if sheep[x][y]=='#' and not check[x][y]:
                while True:
                    for i in range(4):
                        check[x][y] == 1
                        dx=x+dr[i]
                        dy=y+dc[i]
                        if 0<=dx<r and 0<=dy<c and not check[dx][dy] and sheep[dx][dy]=='#':
                            x=dx
                            y=dy
                            num += 1
                            break
    print(num)



