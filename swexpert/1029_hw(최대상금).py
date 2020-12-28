import sys
import collections

sys.stdin = open('input10.txt', 'r')


def check(cnt):
    global ans

    total = int(''.join(number))
    visited.append([cnt, total])

    if cnt == 0:
        if total > ans:
            ans = total
        return

    for i in range(len(number)):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            if [cnt-1, int(''.join(number))] not in visited:    # 들어가있는 건 걸러주자
                check(cnt-1)    # cnt -1
            number[i], number[j] = number[j], number[i]


for tc in range(1, int(input())+1):
    number, k = input().split()
    number = list(number)
    ans = -123456
    visited = []
    check(int(k))
    print('#{} {}'.format(tc, ans))