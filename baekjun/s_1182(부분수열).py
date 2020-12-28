from itertools import combinations

n,s=map(int,input().split())
numbers=list(map(int,input().split()))

ans=0
for i in range(1,n+1):
    num=list(combinations(numbers,i))
    for j in num:
        num=sum(j)
        if num ==s:
            ans+=1
print(ans)

'''
1 3
0
'''