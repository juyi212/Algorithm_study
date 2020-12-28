t=int(input()) #스위치 개수
swit=list(map(int,input().split())) #스위치 상태
swit.insert(0,0)
num=int(input())

for i in range(num):
    person,n=map(int,input().split())
    if person ==1: # 남학생
        for k in range(n,t+1,n):
            if swit[k]==1:
                swit[k]=0
            else:
                swit[k]=1

    else: #여학생
        if swit[n] == 1:
            swit[n] = 0
        else:
            swit[n] = 1
        m=1
        while(n-m>0 and n+m<=t and swit[n-m]==swit[n+m]):
            if swit[n+m]==1:
                swit[n - m]=0
                swit[n + m]=0
            elif swit[n+m]==0:
                swit[n - m]=1
                swit[n + m]=1
            m+=1


for i in range(1,t+1):
    print(swit[i],end=' ')
    if i%20==0:
        print()

