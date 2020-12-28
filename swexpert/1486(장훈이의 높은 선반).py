import sys
sys.stdin = open('input2.txt','r')

def check(idx):
    global max_t
    if idx == n:
        total = 0
        for i in range(n):
            if arr[i] == 1:
                total += peoples[i]
        if total >= height:
            result.append(total)
    else:
        arr[idx] = 1
        check(idx+1)
        arr[idx] = 0
        check(idx+1)


for tc in range(1, int(input())+1):
    n, height = map(int, input().split())
    peoples = list(map(int, input().split()))
    max_t = 0
    arr = [0]*n
    result = []
    check(0)
    print(f'#{tc} {min(result)-height}')