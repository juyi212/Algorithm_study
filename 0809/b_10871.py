n,x=map(int,input().split())
s=list(map(int,input().split()))
v=[]
for i in range(n):
    if s[i]<x:
        v+=[s[i]]
print(*v,sep=" ")