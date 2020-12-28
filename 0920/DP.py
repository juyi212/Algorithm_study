def fibo2(n): # 메모이제이션
    f=[0,1]

    for i in range(2,n+1):
        f.append(f[i-1]+f[n-2])

    return f[n]