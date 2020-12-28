def search(matrix):
    #행
    arr=[]
    for i in range(9):
        check=[0]*9
        for j in range(9):
            if matrix[i][j] in numbers:
                check[matrix[i][j]-1]+=1
        arr.append(check)
    for ar in arr:
        for a in ar:
            if a != 1:
                return 0


    # 열
    arr = []
    for i in range(9):
        check=[0]*9
        for j in range(9):
            if matrix[j][i] in numbers:
                check[matrix[j][i]-1]+=1
        arr.append(check)

    for ar in arr:
        for a in ar:
            if a != 1:
                return 0


    # 사각형
    for i in range(0,9,3):
        for j in range(0,9,3):
            check=[0]*9
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if matrix[x][y] in numbers:
                        check[matrix[x][y]-1]+=1
            arr.append(check)

    for ar in arr:
        for a in ar:
            if a != 1:
                return 0
    return 1

t=int(input())
for tc in range(1,t+1):
    matrix=[list(map(int,input().split())) for _ in range(9)]
    numbers=list(range(1,10))
    print(search(matrix))


'''
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
'''