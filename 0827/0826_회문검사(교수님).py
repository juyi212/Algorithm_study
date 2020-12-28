def find_palindrome(board):
    result = ""  # 회문을 찾으면 반환하기 위한 변수
    # 행 우선 순회
    for i in range(n):
        for j in range(n-m+1):
            #회문검사
            for k in range(m//2):
                if board[i][j+k] != board[i][j+m-1-k]:
                    break
            else:
                result=board[i][j:j+m]
                return result

    for i in range(n):
        for j in range(n-m+1):
            for k in range(m//2):
                if board[j+k][i] != board[j+m-1-k][i]:
                    break
                else:
                    for x in range(j,j+m):
                        result+=board[x][i]
                    return result

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    board=[input() for _ in range(n)]
    result=find_palindrome(board)
    print(result)