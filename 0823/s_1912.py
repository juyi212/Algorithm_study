import sys
n=int(input())
a=list(map(int, sys.stdin.readline().split()))
# 연속된 합, 전의 연속된 합보다 작으면 break, 더 크면 다음 값 더해보기.

total=[0]*(n-1)
for i in range(n-1):
    total[i]+=a[i]+a[i+1]

print(max(total))