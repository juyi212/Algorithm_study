import sys
sys.stdin=open("input_search.txt","r")

T=int(input())
for test_case in range(1,T+1):
    n=int(input()) #길이
    arr=[list(map(int,input().split())) for _ in range(n)]
    total=[]
    count=0
    for x in range(n): #행
        for y in range(n): #열
            if arr[x][y] != 0: #아닐경우 카운트
                col_count=0
                for k in range(y,n): #row고정 col 찾기
                    if arr[x][k]:
                        col_count+=1
                    else:
                        break
                row_count=0
                for k in range(x,n):#col 고정 row 찾기
                    if arr[k][y]:
                        row_count+=1
                    else:
                        break
                for k in range(x, x + row_count): #찾은 것들 o으로 다 바꿔주기.
                    for l in range(y, y + col_count):
                        arr[k][l]=0
                count+=1
                total.append((row_count,col_count,row_count*col_count)) #쌍을 위해서 튜플로 만들어줌.

    for i in range(0,len(total)-1):
        min=i
        for j in range(i+1,len(total)):
            if total[min][2]>total[j][2]: #넓이가 클때
                min=j
            elif total[min][2]==total[j][2]: #넓이가 같을 때
                if total[min][0]>total[j][0]: #row를 비교하고 작은 값으로 변환.
                    min=j
        total[i], total[min] = total[min], total[i]

    print(f'#{test_case} {count}',end=' ')
    for i in range(len(total)): #리스트 안의
        for j in range(0,2):  #튜플 불러내기
            print(total[i][j],end=' ')
    print(end='\n')


