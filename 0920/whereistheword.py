def hi(matrix):
    global cnt
    for i in range(n):
        check = []
        for j in range(n):
            if matrix[i][j]==1:
                check.append(1)
            elif matrix[i][j]==0:
                if check.count(1)==k:
                    cnt+=1
                check=[]

        if len(check)>=k:
            if len(check)==k:
                cnt+=1
    return cnt

t=int(input())
for tc in range(1,t+1):
    n,k=map(int,input().split())
    matrix=[list(map(int,input().split())) for _ in range(n)]
    r_matrix=list(zip(*matrix))
    print(r_matrix)
    check=[]
    cnt=0
    a=hi(matrix)
    cnt = 0
    b=hi(r_matrix)
    print(a,b)
    print(a+b)


'''
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''

'''
1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''