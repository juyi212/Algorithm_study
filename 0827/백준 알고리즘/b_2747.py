import sys
sys.setrecursionlimit(10**7)
def fibo(n):
    if n>=2 and len(f)<=n:
        f.append(fibo(n-1)+fibo(n-2))
    return f[n]

t=int(input())
f=[0,1]
print(fibo(t)%1000000)