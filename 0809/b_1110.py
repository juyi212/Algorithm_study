N=int(input())
if N<10:
    N='0'+str(N)
first=str(N)
n=0
while n<100:
    vv=''
    v = 0
    for i in str(N):
        v+=int(i)
    vv += str(i)
    for j in str(v):
        pass
    vv+=j
    n += 1
    if vv==first:
        break
    N=vv
print(n)