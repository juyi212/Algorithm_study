
def check(num):
    a = int(num, 16)    # 10진수로 바꿔줌
    print(a)
    y = [0] * 4
    for i in range(4):
        y[i] = str(a % 2)
        a //= 2
    y = reversed(y)
    y = ''.join(y)  # 문자열로 만들어줌
    return y


for tc in range(1, int(input())+1):
    n, number = input().split()
    result = ''
    cnt = 0
    value = 0
    for i in range(int(n)):
        result += check(number[i])
    print('#{0} {1}'.format(tc, result))


'''
3
4 47FE
5 79E12
8 41DA16CD
'''