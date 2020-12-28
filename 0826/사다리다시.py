import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")
def sadari(i,j):
    checked[i][j] = 1
    dr=[0,0,-1]
    dc=[1,-1,0]
    if i == 0:
        return f'#{t} {j}'

    for k in range(3):
        x=i+dr[k]
        y=j+dc[k]

        if 0<=x<100 and 0<=y<100 and data[x][y]=='1' and not checked[x][y]:
            return sadari(x,y)

for _ in range(1,11):
    t=int(input())
    data=[list(input().split()) for _ in range(100)]
    checked = [[0] * 100 for _ in range(100)]
    j=data[-1].index('2')
    checked[99][j] = 1
    print(sadari(99,j))