import collections

def dfs(h,n,s): #h=idx, n=정해진 수 사람, s 합
    global min_v
    if n==h:
        if s>= B and min_v>=s-B:
                min_v=s-B
    elif s>=B and min_v<s-B:
        return
    else:
        dfs(h+1,n,s+height[h]) #방문 여부 체크
        dfs(h+1,n,s)

t=int(input())
for tc in range(1,t+1):
    N,B=map(int,input().split())
    height=list(map(int,input().split()))
    visit=[0]*N
    min_v=1000000000000
    dfs(0,N,0)
    print(f'#{tc} {min_v}')

# bfs 전형적인 부분 시간초과남
