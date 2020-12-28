h,m=map(int,input().split())

if h==0:
    if 45 <= m < 60:
        print(h, m - 45)
    else:
        print(23, m + 15)
else:
    if 45 <= m < 60:
        print(h, m - 45)
    else:
        print(h - 1, m + 15)
