def solution(board, moves):
    # n = len(board[0])
    # new = [[0]*n for _ in range(n)]
    # # 굳이 변환 안해도됨..
    # for r in range(n):
    #     for c in range(n):
    #         new[c][n-1-r] = board[r][c]
    here = []
    answer = 0
    # stack 으로 풀기
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                here.append(board[j][i-1])
                board[j][i - 1] = 0

                if len(here) > 1:
                    if here[-1] == here[-2]:
                        here.pop(-1)
                        here.pop(-1)
                        answer += 2
                break

    print(answer)

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)
