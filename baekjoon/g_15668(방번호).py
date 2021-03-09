
number = int(input())

new = ''
Flag = False
for i in range(1, min(100000, number)):
    new = str(i) + str(number-i)
    li = []
    ans = -1
    for w in new:
        if w not in li:
            li.append(w)
        else:
            ans = 0
            exit(0)
    if ans:
        print(number-i, end=' ')
        print('+', end = ' ')
        print(i)
        Flag = True
        break
if not Flag:
    print(-1)



