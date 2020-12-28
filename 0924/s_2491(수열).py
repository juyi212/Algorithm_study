n=int(input())
numbers=list(map(int,input().split()))

cnt=1
max_l=1

for i in range(1,n):
    if numbers[i-1]<=numbers[i]:
        cnt+=1
    else:
        cnt=1
    if max_l<cnt:
        max_l=cnt
cnt=1
for i in range(1,n):
    if numbers[i-1]>=numbers[i]:
        cnt+=1
    else:
        cnt=1
    if max_l<cnt:
        max_l=cnt

print(max_l)


'''
4
1 1 1 1
'''

'''
4
1 3 2 1
'''