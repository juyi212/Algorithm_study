import sys
import collections
sys.stdin = open('input11.txt', 'r')


def check(a, b, idx):
    if idx == 0:
        return a+b
    elif idx == 1:
        return a-b
    elif idx == 2:
        return a*b
    elif idx == 3:
        return int(a/b) # 소수점 이하 날려버리기


def dfs(i, num):
    global min_p, max_p

    if i >= N-1:
        if num < min_p: # 최대 최소 같이 봐주기
            min_p = num
        if num > max_p: # elif 로 처리하면 x
            max_p = num

    for j in range(len(cards)):
        if cards[j]:    # 카드가 있을 경우에만 진행
            cards[j] -= 1
            a = check(num, numbers[i+1], j) # 연산된 값과 연산할 값 넣어주기
            dfs(i+1, a)
            cards[j] += 1


for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))     # + , -, * , /
    numbers = list(map(int, input().split()))
    min_p = 100000000000
    max_p = -123455678989
    dfs(0, numbers[0])
    print('#{} {}'.format(tc, max_p-min_p))

