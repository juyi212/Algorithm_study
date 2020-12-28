n=int(input())

def han(n):
    li=list(str(n))
    v=[]
    for i in range(0,len(li)-1):
        for j in range(i+1,i+2):
            v+=[int(li[i])-int(li[j])]

    for i in range(len(li)-2):
        if v[i]!=v[i+1]:
            return 0
        elif v[i]==v[i+1]:
            continue
    return 1

if n<100:
    print(n)
else:
    count=99
    for i in range(100,n+1):
        k=han(i)
        count+=k
    print(count)