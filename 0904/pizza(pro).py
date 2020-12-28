for tc in range(1,int(input())+1):
    n,m=map(int,input().split()) #n 화덕의 크기, m 피자 수
    pizza=[0]+list(map(int,input().split()))
    oven=[i for i in range(1,n+1)] #피자 번호 집어넣음
    pos=n+1 #추가될 피자 번호
    while len(oven)>1:
        num=oven.pop(0)
        pizza[num]=pizza[num]//2
        if pizza[num]:
            oven.append(num)
        else:
            if pos<=m:
                oven.append(pos)
                pos+=1
    print(f'#{tc} {oven[0]}')

