import sys
sys.stdin = open('input.txt', 'r')


def win(w):
    i = 0
    while i < 10:
        if w[i] >= 3:
            w[i] -= 3
            return True
        if w[i] > 0 and w[i+1] > 0 and w[i+2] > 0:
            w[i] -= 1
            w[i+1] -= 1
            w[i+2] -= 1
            return True
        i += 1


for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    arr1 = [0] * 12
    arr2 = [0] * 12
    point = False
    for i in range(0, len(cards), 2):
        arr1[cards[i]] += 1
        arr2[cards[i+1]] += 1
        if arr1.count(1) >= 3 or arr2.count(1) >= 3:
            w1 = win(arr1)
            if w1:
                print(f'#{tc} {1}')
                point = True
                break
            w2 = win(arr2)
            if w2:
                print(f'#{tc} {2}')
                point = True
                break
    if not point:
        print(f'#{tc} {0}')



'''
1
1 9 1 6 2 6 2 1 3 2 3 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

'''