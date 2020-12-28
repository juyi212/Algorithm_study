import sys
sys.stdin=open("sample_input.txt","r")
#3기 시험문제
T=int(input())
for test_case in range(1,T+1):
    total = [[0] * 10 for _ in range(10)]
    N=int(input())
    for q in range(N):
        a = list(map(int, input().split()))
        x,y=a[0],a[1]
        n,m=a[2],a[3]
        count=0
        for ax in range(x,n+1):
            for ay in range(y,m+ 1):
                total[ax][ay]+=a[-1]
        for i in total:
            for j in i:
                if j ==3:
                    count+=1
    print(f'#{test_case} {count}')

