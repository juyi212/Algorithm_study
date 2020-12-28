t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split()) # n 행 , m 열
    colors=[list(input().rstrip()) for _ in range(n)]
    print(colors)
    min_cnt=2500
    for i in range(0,n-2): # 행의 인덱스 임
        for j in range(i+1,n-1):
            # 여기서 세개 영역으로 구분할 수 있음
            cnt=0
            # 흰색영역 순회하면서 바꿔야할 개수 세기
            # 파
            # 빨
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

    print(min_cnt)