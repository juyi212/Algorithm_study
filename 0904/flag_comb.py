def comb(selected,idx,cnt):
    global result
    if cnt==t:
        a=-1
        b=-1
        for i in range(len(selected)):
            if selected[i]==1:
                if a==-1:
                    a=i
                else:
                    b=i
        check(selected,a,b)
        return
    if idx>=n:
        return
    if idx!=n-1:
        selected[idx]=1
        comb(selected,idx+1,cnt+1)
    selected[idx]=0
    comb(selected,idx+1,cnt)

def check(selected,i,j):
    global min_cnt
    cnt = 0
    num=0 # 1이 나온 개수를 count
    for w in range(0,i+1):
        for k in range(m):
            if colors[w][k]!='W':
                cnt+=1

    for b in range(i+1,j+1):
        for k in range(m):
            if colors[b][k]!='B':
                cnt+=1

    for r in range(j+1,n):
        for k in range(m):
            if colors[r][k]!='R':
                cnt+=1

    if min_cnt>cnt:
        min_cnt=cnt

    return min_cnt


t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split()) # n 행 , m 열
    colors=[list(input().rstrip()) for _ in range(n)]
    result=[]
    selected=[0]*n
    min_cnt=2500
    t=2
    comb(selected,0,0)
    print(f'#{tc} {min_cnt}')

