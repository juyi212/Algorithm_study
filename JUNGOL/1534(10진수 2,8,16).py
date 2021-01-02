num, ch = map(int, input().split())

if ch == 2:
    #    10진수를 2진수로
    result = []
    while True:
        n = num % 2
        result.append(str(n))
        num = num // 2
        if num == 1:
            result.append(str(num))
            break
    r = result[::-1]
    rr = ''.join(r)
    print(rr)
elif ch == 8:
    # o = format(num, 'o')
    # print(o)
    result = []
    while num > 0:
        n = num % 8
        result.append(str(n))
        num = num // 8
    r = result[::-1]
    rr = ''.join(r)
    print(rr)

elif ch == 16:
    result = []
    while num > 0:
        if num % 16 >= 10:
            result.append(chr(num%16+55))
        else:
            result.append(str(num%16))
        num = num // 16
    print(''.join(reversed(result)))