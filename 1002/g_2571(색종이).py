def check():
    global ans
    for i in range(100):
        for j in range(100):
            if matrix[i][j]==0:
                continue
            matrix[i][j]+=matrix[i-1][j] # 현위치에서 밑으로 몇칸?

    for r in range(1,100):
        for c in range(1,100):
            height=100
            for k in range(c,100): #가로로 이동하면서 각 구간의 값 곱하기 가로하면 넓이 나옴.
                if height>0:
                    height=min(height,matrix[r][k])
                    area=height*(k-c+1) #칸개수로 계산
                    ans=max(ans,area)
                else:
                    break
    return ans

def first(y,x): #영역 체크하기
    for i in range(x,x+10):
        for j in range(y,y+10):
            matrix[i][j]=1

t=int(input())
matrix=[[0]*101 for _ in range(101)]
ans=0
for _ in range(t):
    x,y=map(int,input().split())
    first(x,y)
print(check())



'''
4
1 1
1 10
10 1
10 10

'''