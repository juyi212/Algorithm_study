n, m = map(int, input().split())

if 0 > n or n > 100 or m < 0 or m > 3:
    print('INPUT ERROR!')
else:
    if m == 1:
        for i in range(1, n+1):
            print('*' * i)
    elif m == 2:
        for i in range(n, -1, -1):
            print('*' * i)

    elif m == 3:
        for i in range(1, n+1): # 오른쪽부분은 굳이 신경 안써줘도 됨
            for j in range(i, n):
                print(' ', end = '')
            for k in range(1, 2*i):
                print('*', end ='')
            print()

