C,R=map(int,input().split()) #가로 세로

r=[0,R]
c=[0,C]

n= int(input())
for i in range(n):
    s,num=map(int,input().split())
    if s == 0:
        r.append(num)
    else:
        c.append(num)

r.sort()
c.sort()

max_s=0
for i in range(1,len(r)): #하나씩 비교
    for j in range(1, len(c)):
        l=r[i]-r[i-1]
        w=c[j]-c[j-1]
        max_s=max(max_s,l*w)

print(max_s)

'''
10 8
2
0 0
1 0

'''
'''
10 10
2
0 5
1 5
'''