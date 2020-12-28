import sys
sys.stdin = open('input7.txt', 'r')

number = {'211': 0, '221':1, '122':2, '411':3, '132':4, '231':5, '114':6, '312':7, '213':8, '112':9}


# conversion = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
#          '4':'0100', '5':'0101', '6':'0110', '7':'0111',
#          '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
#          'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

for tc in range(1, int(input())+1):
    w, h = map(int, input().split())
    matrix = [input() for _ in range(w)]
    result = [''] * w
    for i in range(w):
        for j in range(h):
            result[i] += format(int(matrix[i][j], 16), 'b').zfill(4)

    sum_result = 0
    total = []
    visited = []

    for arr in result:
        idx = len(arr) - 1
        a = b = c = 0
        while idx >= 0:
            if b == 0 and c == 0 and arr[idx] == '1':
                a += 1
                idx -= 1
            elif a > 0 and c == 0 and arr[idx] == '0':
                b += 1
                idx -= 1
            elif a > 0 and b > 0 and arr[idx] == '1':
                c += 1
                idx -= 1
            elif a == 0 and b == 0 and c == 0 and arr[idx] == '0':
                idx -= 1
            elif a > 0 and b > 0 and c > 0 and arr[idx] == '0':
                min_num = min(c, b, a)
                c = c // min_num
                b = b // min_num
                a = a // min_num
                st = str(c) + str(b) + str(a)
                total.append(number[st])
                a = b = c = 0

            if len(total) == 8:
                total = total[::-1]
                sum_t = (total[0] + total[2] + total[4] + total[6]) * 3 \
                        + (total[1] + total[3] + total[5]) + total[7]
                if sum_t % 10 == 0 and total not in visited:
                    sum_result += sum(total)
                visited.append(total)
                total = []

    print('#{} {}'.format(tc, sum_result))

'''
90577156
[0, 9, 4, 8, 8, 2, 4, 3]
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