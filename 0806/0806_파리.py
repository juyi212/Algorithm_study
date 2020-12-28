import sys
sys.stdin=open("input_hw.txt","r")

T=int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    a=[]
    for i in range(N):
        a.append(list(map(int, input().split())))
    li=[]
    for rr in range(N-M+1):
        for cc in range(N-M+1):
            sum1 = 0
            for ar in range(M):
                for ac in range(M):
                    sum1+=a[rr+ar][cc+ac]
            li.append(sum1)
    print(f'#{test_case} {max(li)}')

    # nv=[[0]*M for _ in range(M)]
    # print(nv)
    # for i in range(0,len(pari)-N):
