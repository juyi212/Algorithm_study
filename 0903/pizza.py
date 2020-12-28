def bake():
    q=[]
    for i in range(m):
        q.append((cheeses[i],i))
        while len(q)==n:
            first,idx = q.pop(0)
            if first // 2 != 0:
                q.append((first // 2,idx))
            else:
                break
    while True:
        if len(q)<n:
            first, idx = q.pop(0)
            if first // 2 != 0:
                q.append((first // 2, idx))
            elif len(q)==1:
                first,idx=q.pop()
                return idx+1
                break

t=int(input())

for tc in range(1,t+1):
    n,m=map(int,input().split()) # n 화덕의 크기 . m 피자의 개수
    cheeses=list(map(int,input().split()))
    print(f'#{tc} {bake()}')

'''
1
5 10
20 4 5 7 3 15 2 1 2 2

'''