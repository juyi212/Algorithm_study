import sys
sys.stdin=open('sample_input_sum.txt','r')


T = int(input())
for test_case in range(1,T+1):
    N,M= map(int, input().split())
    li = list(map(int, input().split()))
    a=[]
    for i in range(len(li)-M+1):
        sum = 0
        sum += li[i]
        for j in range(i+1,i+M):
            sum += li[j]
        a+=[sum]
    print(f'#{test_case} {max(a)-min(a)}')