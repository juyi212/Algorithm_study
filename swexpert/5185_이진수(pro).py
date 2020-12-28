hex_dic = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def check(num):
    y = [0] * 4
    for i in range(4):
        y[i] = str(num % 2)
        num //= 2
    y = reversed(y)
    y = ''.join(y)  # 문자열로 만들어줌

    return y


for tc in range(1, int(input())+1):
    n, number = input().split()
    result = ''
    value = ''
    for i in range(int(n)-1, -1, -1):
        result = check(hex_dic[number[i]]) + result
    print('#{0} {1}'.format(tc, result))
