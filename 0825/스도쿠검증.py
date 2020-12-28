def check_sudoku(sudoku):
    # check 배열 : 숫자가 한 번씩 나오는지 검사하는 배열
    # 모든 행  i in range(9):검사
    for i in range(9):
        check=[0] *10
        for j in range(9):
            if check[sudoku[i][j]]==0:
                check[sudoku[i][j]] == 1
            else: # 숫자 중복 발생 >> 스도쿠 아님
                return 0

    for i in range(9):
        check=[0] *10
        for j in range(9):
            if check[sudoku[j][i]]==0:
                check[sudoku[j][i]] == 1
            else: # 숫자 중복 발생 >> 스도쿠 아님
                return 0

    # 3*3 행렬 9개 검사
    for i in range(0,9,3):
        for j in range(0,9,3):
            for r in range(i,i+3):
                for c in range(i,i+3):
                    check = [0] * 10
                    if check[sudoku[r][c]]==0:
                        check[sudoku[r][c]] == 1
                    else: # 숫자 중복 발생 >> 스도쿠 아님
                        return 0
    return 1


t= int(input())
for tc in range(1,t+1):
    sudoku=[list(map(int,input().split())) for _ in range(9)]
    result= check_sudoku(sudoku)
    print(f'#{tc} {result}')

