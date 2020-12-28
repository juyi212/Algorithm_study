c=int(input())

for cc in range(c):
    n=list(map(int,input().split()))
    total=0
    for i in range(1,len(n)):
        total+=n[i]
    s=total/n[0]
    count=0
    for i in range(1,len(n)):
        if n[i]>s:
            count+=1
    print(f'{(count/n[0])*100:.3f}%')