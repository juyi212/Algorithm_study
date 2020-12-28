n = int(input())
li = [[0]*n for _ in range(n)]

if n % 2 == 0 or n < 1 or n > 100:
    print('INPUT ERROR')
else:
    num = 64
    for i in range((n//2)+1, -1, -1): # 반띵
        for j in range(i, n-i): # 3, 2-4 1-5
            if num <90:
                num += 1
                li[j][i] = chr(num)
            else:
                num = 65
                li[j][i] = chr(num)


    for i in range(n):
        for j in range(n):
            if li[i][j] == 0:
                print('', end =' ')
            else:
                print(li[i][j], end = ' ')
        print()