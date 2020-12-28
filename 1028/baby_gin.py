wow = ['124783', '667767', '054060', '101123']

# baby-jin 완전 탐색으로 풀기
# 조합으로 풀어보기 6가지 중에 3가지 숫자를 선택 1,2,4   3,7,8
n = 6
k = 3
arr = [0] * n


def comb(idx, cnt):
    if cnt == k:    # 조합에 포함되는 모든 요소를 선택했다.
        print(arr)
        return
    if idx == n:
        return
    # idx에 해당하는 요소를 조합에 포함할지 안할지 결정
    arr[idx] = 1
    comb(idx+1, cnt+1)
    arr[idx] = 0
    comb(idx+1, cnt)

comb(0, 0)
