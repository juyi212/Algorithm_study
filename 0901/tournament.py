def game(s,e):
    if s == e: # s와 e가 같다 = 한 명인 그룸
        return s
    # 절반씩 나누어서 게임 실행
    # 앞부분 승자, 뒷부분 승자 각각 구함.
    # 승자를 결정한다.

    center=(s+e)//2
    v1=game(s,center)
    v2=game(center+1,e)

    v1_card=cards[v1]
    v2_card=cards[v2]
    if v1_card ==1: # 가위
        if v2_card==2 : # 바위
            return v2
        else:
            return v1
    elif v1_card==2: #바위
        if v2_card==3: # 보
            return v2
        else:
            return v1

    elif v1_card==3: #보
        if v2_card==1: #가위
            return v2
        else:
            return v1

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    cards=list(map(int,input().split()))
    result=game(0,n-1)
    print(f'#{tc} {result+1}')