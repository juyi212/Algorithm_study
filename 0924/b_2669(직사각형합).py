matrix=[[0]*101 for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            matrix[i][j]=1
s=0
for i in matrix:
    s+=i.count(1)
print(s)
'''
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''