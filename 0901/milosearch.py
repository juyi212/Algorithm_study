def check(i,j):
    global ans
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    for k in range(4):
        nr=i+dr[k]
        nc=j+dc[k]
        if 0<=nr<n and 0<=nc<n and milo[nr][nc]==0 and not (nr,nc) in stack:
            stack.append((nr,nc))
            check(nr,nc)
            stack.pop()
        if 0<=nr<n and 0<=nc<n and milo[nr][nc]==3 and not (nr,nc) in stack:
            ans+=1
            return

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    milo=[list(map(int,input().rstrip())) for _ in range(n)]
    stack=[]
    ans=0
    for i in range(n-1,0,-1):
        for j in range(n):
            if milo[i][j]==2:
                stack = [(i, j)]
                if check(i,j):
                    print(f'#{tc} {ans}')
                    break
                else:
                    print(f'#{tc} {ans}')



'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''