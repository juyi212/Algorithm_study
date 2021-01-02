def check(n, m):
    result = []
    while n > 0:
        if m >= 10 and n % m >= 10:  # 변환하는 수가 10보다 클 때
            result.append(chr(n % m + 55))
        else:
            result.append(str(n % m))
        n = n // m
    return ''.join(list(reversed(result)))


while True:
    ch = list(input().split())  # a -> b
    if ch[0] == '0':
        break
    elif ch[1] == '0':
        print('0')
    else:
        num = int(ch[1], int(ch[0]))  # a -> 10진수로
        print(check(num, int(ch[2])))  # 10진수 -> b
