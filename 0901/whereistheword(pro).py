#한 줄에 대해서는 이중 배열로 보는 것이 아니다
t=int(input())
for tc in range(1,t+1):
    n,k=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(n)]
    cnt=0 # 단어가 들어갈 수 있는 개수를 세기 위한 변수

    # 행 조사
    for i in range(n):
        length=0
        for j in range(n):
            # 1이 나오면 길이 +1
            if board[i][j]==1: #1이 나오면 stack에 append
                length+=1
            else: # 0이 나오면 길이 검사 후 길이를 0으로 만듬
                if length ==k: # 스택 길이를 검사
                    cnt+=1
                length=0 # stack이 빌때 까지 pop
        if length==k:
            cnt+=1

    # 열 검사
    for i in range(n):
        length=0
        for j in range(n):
            # 1이 나오면 길이 +1
            if board[j][i]==1:
                length+=1
            else:
                if length ==k:
                    cnt+=1
                length=0
        if length==k:
            cnt+=1
    print(cnt)