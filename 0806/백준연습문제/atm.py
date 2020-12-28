N=int(input())
M= list(map(int,input().split()))
for i in range(0,len(M)-1):
    min=i
    for j in range(i+1,len(M)):
        if M[min]>M[j]:
            min=j
    M[i],M[min]=M[min],M[i]
print(M)
x=[]
sum1=0
sum2=0
for j in M:
    sum1+=j
    x.append(sum1)
for z in x:
    sum2+=z
print(sum2)


