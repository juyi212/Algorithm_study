def d(n):
    a=0
    for i in list(str(n)):
        a=a+int(i)
    return n+a

li=[]
for i in range(1,10001):
    k=d(i)
    li.append(k)

total=[]
for i in range(1,10001):
    if i in li:
        pass
    else:
        print(i)