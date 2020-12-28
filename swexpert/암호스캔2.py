import sys
sys.stdin = open('input7.txt', 'r')

number = {'211': '0', '221' : '1', '122': '2', '411': '3', '132': '4', '231': '5', '114': '6', '312': '7', '213': '8',
          '112': '9'}

def check(arr):
    global wow
    j = len(arr) - 1
    total = ''
    tmp_li = []
    while j >= 0:
        if arr[j] == '1':
            cnt = 1
            tmp = []
            for k in range(j - 1, -1, -1):
                if arr[k] == arr[k + 1]:
                    cnt += 1
                else:
                    tmp.append(cnt)
                    cnt = 1
                if len(tmp) == 3:
                    j -= sum(tmp)
                    tmp_li.append(tmp)
                    min_tmp = min(tmp)
                    for l in range(3):
                        tmp[l] = tmp[l] // min_tmp
                    tmp = []
                    break
        # n2, n3, n4 = 0, 0, 0
        # while arr[i] == '1' and i > -1:
        #     n4 += 1
        #     i -= 1
        # while arr[i] == '0' and i > -1:
        #     n3 += 1
        #     i -= 1
        # while arr[i] == '1' and i > -1:
        #     n2 += 1
        #     i -= 1
        # while arr[i] == '0' and i > -1:
        #     i -= 1
        #
        # min_n = min(n2, n3, n4)
        # a = n2 // min_n
        # b = n3 // min_n
        # c = n4 // min_n
        # g = str(a) + str(b) + str(c)
            if tmp_li:
                aaa = list(map(str, tmp_li.pop()))
                g = ''.join(aaa)
                total += number[g]
            if len(total) == 8:
                total = total[::-1]
                if total not in wow:
                    wow.append(total)
                total = ''
            wow = list(set(wow))
        else:
            j -= 1
    return


t = int(input())
for tc in range(1, t+1):
    w, h = map(int, input().split())
    matrix = [input() for _ in range(w)]
    re = list()
    wow = list()
    for i in matrix:
        new = ''
        for j in range(len(i)):
            if i[j].isdigit():  # 숫자이면
                new += format(int(i[j]), 'b').zfill(4)
            else:
                new += format(int(i[j], 16), 'b').zfill(4)
        if new.strip('0') == '':
            pass
        else:
            re.append('0'+new.strip('0'))
    re = list(set(re))
    for i in re:
        check(i)

    sum_result = 0
    for j in wow:
        result = list(map(int, j))
        sum_t = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1] + result[3] + result[5]) + result[7]
        if sum_t % 10 == 0:
            re = 0
            for mm in range(len(j)):
                re += int(j[mm])
            sum_result += re
    print('#{} {}'.format(tc, sum_result))
