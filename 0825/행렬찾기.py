import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for test_case in range(1,T+1):
    n=int(input()) #길이
    arr=[list(map(int,input().split())) for _ in range(n)]
    total=[]
    count=0
    for x in range(n): #행
        for y in range(n): #열
            if arr[x][y] != 0:
                col_count=0
                for k in range(y,n):
                    if arr[x][k]:
                        col_count+=1
                    else:
                        break
                row_count=0
                for k in range(x,n):
                    if arr[k][y]:
                        row_count+=1
                    else:
                        break
                for k in range(x, x + row_count):
                    for l in range(y, y + col_count):
                        arr[k][l]=0
                count+=1
                total.append((row_count,col_count,row_count*col_count))


    for i in range(len(total)):
        for j in range(len(total)-1-i):
            if total[j][2] > total[j+1][2]:
                total[j], total[j+1] =total[j+1], total[j]

            elif total[j][2] == total[j + 1][2]:
                if total[j][0]>total[j+1][0]:
                    total[j], total[j+1] =total[j+1], total[j]

    print("#{}".format(test_case), end=" ")
    print(len(total), end=" ")
    for i in range(len(total)):
        print(total[i][0],total[i][1],end=" ")