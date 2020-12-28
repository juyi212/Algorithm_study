t=int(input())
for tc in range(1,t+1):
    n,k=map(int,input().split())
    numbers=list(range(1,13))
    result=[]
    for i in range(1<<12): #1<<n : 부분 집합의 개수
        li=[]
        for j in range(13): # 원소의 수만큼 비트를 비교함.
            if i &(1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
                li.append(numbers[j])
        result.append(li)
    count=0
    for i in result:
        if len(i)==n:
            if sum(i)==k:
                count+=1
    print(f'#{tc} {count}')

