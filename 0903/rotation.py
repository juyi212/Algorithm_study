t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    numbers=list(map(int,input().split()))
    num=0
    while num<=m:
        v=numbers.pop(0)
        numbers.append(v)
        num+=1
    print(f'#{tc} {numbers[-1]}')
