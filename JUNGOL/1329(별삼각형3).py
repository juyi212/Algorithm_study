n = int(input())

if n % 2 == 0 or n < 0 or n > 100:
    print('INPUT ERROR!')
else:
    left ,right = 0, n
    for i in range(n):
        for j in range(left):
            print(' ', end ='')
        for k in range(2*left+1):
            print('*', end = '')
        for m in range(right):
            print(' ', end ='')
        print()

        if i < (n//2):
            left += 1
            right -= (2*left)+1
        else:
            left -= 1
            right += (2 * left) + 1
