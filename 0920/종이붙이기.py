t=int(input())

def dpdp(n):
    if n==1:
        return 1
    if n==2:
        return 3
    return dpdp(n-1)+2*dpdp(n-2)

for tc in range(1,t+1):
    n=int(input())
    print(dpdp(n//10))