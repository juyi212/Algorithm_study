n, m = map(int, input().split())

if 0 >= n or n > 100 or m <= 0 or m > 4 or n % 2 == 0:
    print('INPUT ERROR!')

else:
    if m == 1:
        right = 1
        for i in range(1, n+1):
            for j in range(1, right+1):
                print('*', end ='')
            print()
            if i < (n//2)+1:
                right += 1
            else:
                right -= 1
    elif m == 2:
        left, right = (n//2)+1, (n//2)+1
        for i in range(1, n + 1):
            for j in range(left):
                print(' ',end = '')
            for k in range(left, right):
                print('*',end ='')
            print()
            if i < (n // 2) + 1:
                left -= 1
            else:
                left += 1
    elif m == 3:
        left, right = 0, 0
        for i in range(1, n+1):
            for j in range(left):
                print(' ',end ='')
            for k in range(n-left-right):
                print('*', end ='')
            for r in range(right):
                print(' ', end = '')
            print()
            if i < (n//2)+1:
                left += 1
                right += 1
            else:
                left -= 1
                right -= 1

    elif m == 4:
        left, right = 0, n//2+1
        for i in range(1, n+1):
            for k in range(left):
                print(' ', end ='')
            for j in range(left, right):
                print('*', end ='')
            print()
            if i < (n // 2) + 1:
                left += 1
            else:
                right += 1
