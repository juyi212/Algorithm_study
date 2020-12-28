import sys
sys.setrecursionlimit(10**7)

def dfs(i,j):
    check[i][j]=1
    dr =[0 ,1 ,0 ,-1]
    dc =[1 ,0 ,-1 ,0]  # 우하좌상 i= 0

    for k in range(4):
        x= i+dr[k]
        y= j+dc[k]
        if x<0 or x>=r or y<0 or y>=c:
            continue
        if not check[x][y] and sheep[x][y] =='#':
            dfs(x,y)

T=int(input())
for _ in range(T):
    r,c= map(int,input().split())
    sheep=[list(input().strip()) for _ in range(r)]
    check=[[0]*c for _ in range(r)]
    num=0
    for i in range(r):
        for j in range(c):
            if not check[i][j] and sheep[i][j]=='#':
                dfs(i,j)
                num+=1
    print(num)
 # 확인했다는 것을 알려주는 리스트나 # 을 없애는 방법으로 넣기