def hex_to_dec(num16):
    value = 0

    for i in range(len(num16)):
        if '0' <= num16[i] <= '9':
            tmp = ord(num16[i]) - ord('0')
        else:
            tmp = ord(num16[i]) - ord('A')+10
        value += tmp * (16 ** (count-1-i))



for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    count = N//4
    result = set()
    secret = list(input())

    for k in range(N//4):
        n = secret.pop()
        secret.insert(0, n)
        for i in range(0, N, count):
            a = ''.join(secret[i:i+count])
            result.add(a)

    my_list = []
    for i in result:
        my_list.append(int(i, 16))
    my_list.sort(reverse=True)
    print(f'#{tc} {my_list[K-1]}')

'''
5
12 10
1B3B3B81F75E
'''