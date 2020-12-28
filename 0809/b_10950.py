T=int(input())
c=[]
for test_case in range(T):
    a,b=map(int,input().split())
    c.append(a+b)

for i in c:
    print(i)