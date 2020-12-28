def paper(n):
    for i in range(3,n+1):
        f.append(f[i-1]+(2*f[i-2]))
    return f[n]

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    f=[0,1,3]
    c=paper(n//10)
    print(f'{tc} {c}')