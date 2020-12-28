#오셀로
def init():
    st=n//2
    board[st][st]=board[st+1][st+1]=2
    board[st][st+1]=board[st+1][st]=1
    return board


t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    board=[[0]*(n+1) for _ in range(n+1)]
    # 초기돌의 위치
    init()
    dy=[0,1,1,1,0,-1,-1,-1]
    dx=[-1,-1,0,1,1,1,0,-1]
    for i in range(m):
        c,r,v=map(int,input().split())
        board[c][r]=v
        for k in range(8):
            ny=c+dy[k]
            nx=r+dx[k]
            while True:
                if 0<nx<=n and 0<ny<=n and board[ny][nx]==v and board[ny][nx]!=0: #0이 아니고 자신과 같다면
                    while ny!= c or nx!= r: # 전 값들을 바꿔줘야하니깐 다시 왔던대로 델타값을 빼주고 값을 넣어줌
                        ny-=dy[k]
                        nx-=dx[k]
                        board[ny][nx]=v
                    else: # 바뀜
                        break
                elif nx<=0 or nx>n or ny<=0 or ny>n:
                    break
                elif board[ny][nx] == 0: #11102 이런경우 방지
                    break
                else: # 한방향으로 쭉쭉
                    ny+=dy[k]
                    nx+=dx[k]

    b=0
    w=0
    for i in board:
        b+=i.count(1)
        w+=i.count(2)
    print(f'#{tc} {b} {w}')


# while 문으로 풀기
# n=8
# r=4
# c=5
#
# board=[[0]*(n+1) for _ in range(n+1)]
# dr=[-1,-1,0,1,1,1,0,-1]
# dc=[0,1,1,1,0,-1,-1,-1]
#
# for i in range(8):
#     nr= R
#     nc= C
#     # 한 방에 대해서 전부 1로 바꿔주고 나서 다음 방향에 대해서 1로 바꿔주자
#     # nr, nc에 현재 방향의 델타를 계속 더해주면서 연결이 끝나기 전까지 델타 증가
#     while True:
#         # 범위가 벗어날때까지 nr과 nc를 증가시켜준다.
#         if 0< nr <=N  and 0<nc<=N:
#             board[nr][nc]=1
#             nr+=dr[i]
#             nc+=dc[i]
#         else:
#             break
#
