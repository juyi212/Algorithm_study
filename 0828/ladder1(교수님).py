T=10
#시작지점을 찾으면, dfs를 실행해서 목적지까지

def dfs():
    global ladder
    dr=[0,0,1]
    dc=[-1,1,0]
    for i in range(100):
        if ladder[0][i]==1:
            visited=[[0]*100 for _ in range(100)]
            stack=list()
            stack.append((0,i)) #시작지점 스택에 넣기
            while stack:
                cr,cc=stack.pop()
                visited[cr][cc]=1
                for d in range(3):
                    nr=cr+dr[d]
                    nc=cc+dc[d]
                    if 0<=nr<100 and 0<=nc<100 and visited[nr][nc]==1:
                        if ladder[nr][nc] ==1 :
                            stack.append((nr,nc))
                            break # 더이상 경로를 검사하지 않음
                        elif ladder[nr][nc]==2:
                            return i

for tc in range(1,T+1):
    tc=int(input())
    ladder=[list(input()) for _ in range(100)]
    print(f"{tc} {dfs()}")
