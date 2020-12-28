N=int(input())
p=[]
for i in range(N):
    arr=list(map(int,input().split()))
    p.append(arr)
rank=[1]*N
print(p)
for i in range(N):
    for j in range(N):
        if p[i][0]>p[j][0] and p[i][1]>p[j][i]:
            rank[i]+=1

for i in range(N):
    print(rank[i],end='')

