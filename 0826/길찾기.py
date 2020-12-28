def f1(n):
    global ans
    if n>=0:
        if n==99:
            ans=1
        f1(ch1[n1])
        f1(ch2[n2])

for _ in range(10):
    tc,E = map(int,input().split())
    tmp=list(map(int, input().split()))
    ch1=[-1]*100 #출발점을 인덱스로 도착의 번호룰 저장
    ch2=[-1]*100
    for i in range(E): # 단방향이기때문에 2개의 노드로 정해줌.
        n1=tmp(i*2)
        n2=tmp(i*2+1)
        if ch1[n1]==-1 : #첫 도착지면
            ch1[n1]=n2
        else:
            ch2[n1]=n2
    ans=0
    f1(0)