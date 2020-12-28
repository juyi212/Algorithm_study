def check_pal(m): #회문의 길이를 입력받아서 해당 길이의 회문이 있는지 없는지 판단.
    for i in range(100):
        for j in range(100-m+1):
            #회문검사 대상 뽑아내기
            tmp=board[i][j:j+m] #가로
            tmp2=zboard[i][j:j+m] #세로
            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return True
    return False

for _ in range(10):
    tc=int(input())
    board=[input() for _ in range(100)]
    zboard=list(zip(*board))
    result=0
    # 가장 긴 회문을 찾으면 되니까, 긴 것부터 검사를 하면 된다.
    for i in range(100,0,-1):
        if check_pal(i):
            result=i
            break
    print(f'#{tc} {result}')





# '''
# 1 2 3
# 2 3 4
# 4 5 6
# '''
#
# arr=[[1,2,3],[2,3,4],[4,5,6]]
# test=list(zip(*arr)) # 전치행렬로 만들어줌
# print(test)