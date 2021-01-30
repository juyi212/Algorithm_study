while True:
    num = input()

    if num == '0':
        break
    elif num[::-1] == num:
        print('yes')
    else:
        print('no')


'''
def check(str):
    length =  len(str)
    for i in range(0, length):
        if (str[i] != str[length -i -1]):
            return 'no'
    return 'yes'

'''