def solution(board, moves):
    n = len(board[0])
    new = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new[c][n-1-r] = board[r][c]
    print(new)
    here = []
    answer = 0

    for i in moves:
        for j in range(n-1, -1, -1):
            if new[i-1][j] != 0:
                if len(here) >= 1:
                    if new[i-1][j] == here[-1]:
                        here.pop()
                        new[i - 1][j] = 0
                        answer += 1
                        break
                    else:
                        here.append(new[i-1][j])
                        new[i - 1][j] = 0
                        break
                else:
                    here.append(new[i-1][j])
                    new[i-1][j] = 0
                    break
    print(answer)

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)
