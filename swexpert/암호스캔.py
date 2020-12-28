import sys
sys.stdin = open('input7.txt', 'r')


def check():
    global wow
    i = len(arr) - 1
    total = ''
    while i >= 0:
        n2, n3, n4 = 0, 0, 0
        while arr[i] == '1' and i > -1:
            n4 += 1
            i -= 1
        while arr[i] == '0' and i > -1:
            n3 += 1
            i -= 1
        while arr[i] == '1' and i > -1:
            n2 += 1
            i -= 1
        while arr[i] == '0' and i > -1:
            i -= 1
        min_n = min(n2, n3, n4)
        if min_n != 0:
            total += number[(n2//min_n, n3//min_n, n4//min_n)]
        if len(total) == 8:
            total = list(total)
            total = total[::-1]
            total = ''.join(total)
            if total not in wow:
                wow.add(total)
            total = ''
    return


number = {
    (2, 1, 1): '0',
    (2, 2, 1): '1',
    (1, 2, 2): '2',
    (4, 1, 1): '3',
    (1, 3, 2): '4',
    (2, 3, 1): '5',
    (1, 1, 4): '6',
    (3, 1, 2): '7',
    (2, 1, 3): '8',
    (1, 1, 2): '9',
}

Conversion = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
         '4':'0100', '5':'0101', '6':'0110', '7':'0111',
         '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
         'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

for tc in range(1, int(input())+1):
    w, h = map(int, input().split())
    matrix = [input() for _ in range(w)]
    result = set()
    wow = set()
    for i in matrix:
        new = ''
        for j in range(len(i)):
            new += Conversion[i[j]]

            # tmp = format(int(i[j], 16), 'b')
            # if len(tmp) < 4:
            #     tmp = (4 - len(tmp)) * '0' + tmp
            #     # new += format(int(i[j]), 16).zfill(4)
            # new += tmp
        # new = list(new)
        # # print(new)
        # if new.count('1'):
        #     while True:
        #         if new[-1] == '0':
        #             new.pop()
        #         else:
        #             break
        #
        #     while True:
        #         if new[0] == '0':
        #             new.pop(0)
        #         else:
        #             break
        # new = ''.join(new)
        # result.add(new)
        if new.strip('0') == '':
            pass
        else:
            result.add(new.strip('0'))

    for arr in result:
        check()

    sum_result = 0
    for j in wow:
        result = list(map(int, j))
        print(result)
        sum_t = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1] + result[3] + result[5]) + result[7]
        if sum_t % 10 == 0:
            re = 0
            for mm in range(len(j)):
                re += int(j[mm])
            sum_result += re
    print('#{} {}'.format(tc, sum_result))

'''
1
16 26
00000000000000000000000000
00000000000000000000000000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
000000001DB176C588D26EC000
00000000000000000000000000
00000000000000000000000000
'''