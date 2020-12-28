import sys

sys.stdin = open('input.txt','r')

for tc in range(1, int(input())+1):
    t = int(input())
    numbers = list(map(int, input().split()))
    cnt = [0] * 101
    for i in numbers:
        cnt[i] += 1

    max_c = -1
    max_num = 0
    for i in range(len(cnt)):
        if cnt[i] > max_c:
            max_c = cnt[i]
            max_num = i
        elif cnt[i] == max_c:
            max_num = max(max_num, i)

    print(f'#{tc} {max_num}')