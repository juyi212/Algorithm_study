n = int(input())

arr = [[' ']*(2*n) for _ in range(2*n)]

start = 65

x, y = 0, n-1
num = n-1

while True:
    for i in range(num):
        if start > 90:
            start = 65

        arr[x][y] = chr(start)
        start += 1
        x += 1
        y -= 1

    for i in range(num):
        if start > 90:
            start = 65

        arr[x][y] = chr(start)
        start += 1
        x += 1
        y += 1

    for i in range(num):
        if start > 90:
            start = 65
        arr[x][y] = chr(start)
        start += 1
        x -= 1
        y += 1

    for i in range(num):
        if start > 90:
            start = 65
        arr[x][y] = chr(start)
        start += 1
        y -= 1
        x -= 1

    x += 1
    num -= 1

    if num == 0:
        if start > 90:
            start = 65
        arr[x][y] = chr(start)
        start += 1
        break


for i in range(2*n-1):
    for j in range(2*n-1):
        if arr[i][j] != ' ':
            print(arr[i][j], end = ' ')
        else:
            print(' ', end =' ')
    print()