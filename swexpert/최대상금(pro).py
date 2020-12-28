import sys
sys.stdin = open('input10.txt', 'r')


def check(cnt):
    global ans

    total = int(''.join(number))
    if total in visited[cnt]:   # 그 횟수(cnt)에서 total이 있다면 더 이상 나올 필요 x
        return
    else:
        visited[cnt].add(total) # 없으면 넣어주자

    if cnt == int(k):   # 다 돌렸을때의 최대를 정해줘야함
        if total > ans:
            ans = total
        return

    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            number[i], number[j] = number[j], number[i]
            check(cnt+1)
            number[i], number[j] = number[j], number[i]


for tc in range(1, int(input())+1):
    number, k = input().split()
    number = list(number)
    ans = -123456
    visited = [set() for _ in range(int(k)+1)]
    check(0)
    print('#{} {}'.format(tc, ans))