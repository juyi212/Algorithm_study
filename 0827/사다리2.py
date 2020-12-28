import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input_sadari.txt", "r")
def sadari(i,j):
    global num
    checked[i][j] = 1
    dr=[0,0,-1]
    dc=[1,-1,0]
    for k in range(3):
        x=i+dr[k]
        y=j+dc[k]
        if 0<=x<100 and 0<=y<100 and data[x][y]=='1' and not checked[x][y]:
            num += 1
            return sadari(x,y)
    if i==0:
        min_d[y] = num

for _ in range(1,11):
    t=int(input())
    data=[list(input().split()) for _ in range(100)]
    min_d=[10000]*100
    for j in range(100):
        checked = [[0] * 100 for _ in range(100)]
        if data[99][j]=='1' and not checked[99][j]:
            num=0
            sadari(99,j)
    min_v=min(min_d)
    print(f'#{t} {min_d.index(min_v)}')



#사다리 1
# def check(x,y):
    #if 0<=x<100 and 0<=y<100 and arr[x][y]==1:
    # arr[x][y] == 0
    # return True
# x=y=0
# for i in range(100):
#     if arr[99][i]==2:
#         x,y = 99,i
#         break
# while x: x가 0이되면 나옴
#     arr[x][y]=0
#     if check(x,y-1):
#           y-=1
#     elif check(x,y+1):
#           y+=1
#     else:
#           x-=1

