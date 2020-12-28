n, m = map(int, input().split())


if 0 > n or n > 100 or n % 2 ==0 or m < 1 or m > 3:
    print('INPUT ERROR!')
else:
    if m == 1:
        num = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                num = num + i
                temp = num
                for j in range(temp, temp-i, -1):
                    print(j, end=' ')
            else:
                for k in range(i):
                    num += 1
                    print(num, end =' ')
            print()
    elif m == 2:
        left, right,num= 0, 0, 0
        for i in range(n, -1, -1):
            for m in range(left):
                print(' ', end=' ')
            for j in range(2*i-1):
                print(num, end =' ')
            for k in range(right):
                print(' ', end =' ')
            print()
            num += 1
            left += 1
            right += 1

    elif m == 3:
        end = 1
        for i in range(n):
            num = 0
            for j in range(end):
                num += 1
                print(num, end =' ')
            print()
            if i < n//2 :
                end += 1
            else:
                end -= 1
