def plus(a,b):
    q=[]
    sentence=''
    q.append((a,b,0,matrix[a][b]))
    cnt=0
    while q:
        a,b,cnt,sentence=q.pop(0)
        if cnt>=6:
            result.add(sentence)
            continue #6이상인 것은 넣어주고 다음 단계 말고 다시 stack에 쌓인 것을 봐야함
        for dx,dy in [(0,1),(-1,0),(1,0),(0,-1)]:
            nx,ny=a+dx,b+dy
            if 0<=nx<4 and 0<=ny<4:
                q.append((nx,ny,cnt+1,sentence+matrix[nx][ny]))
    return

t=int(input())
for tc in range(1,t+1):
    matrix=[list(input().split()) for _ in range(4)]
    result=set()
    for i in range(4):
        for j in range(4):
            plus(i,j)
    print(f'#{tc} {len(result)}')
