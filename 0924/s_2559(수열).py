N,K=map(int,input().split())
numbers=list(map(int,input().split()))

s=0
for i in range(K):
    s+=numbers[i]

max_s=s
for j in range(1,(N-K)+1):
    s+=numbers[j+(K-1)]
    s-=numbers[j-1]
    if max_s<s:
        max_s=s
print(max_s)


'''
10 1
3 -2 -4 -9 0 3 7 13 8 -3
'''
'''
10 5
0 0 0 0 0 0 0 0 0 0

10 2
3 -2 -4 -9 0 3 7 13 8 -3

2 1
0 -100
'''

