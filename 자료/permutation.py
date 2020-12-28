# idx : 인덱스
# used : 이미 순열을 만드는데 사용되었는지 체크하는 배열
# perm_arr : 순열을 저장할 배열
def perm(idx, N):
    if idx >= N:
        total = []
        for i in range(N):
            if used[i] == 1:
                total.append(arr[i])
        if sum(total) == 10:
            print(total)
        return

    used[idx] = 1
    perm(idx+1, N)
    used[idx] = 0
    perm(idx+1, N)


arr = [1,2,3,4,5,6,7,8,9,10]
N = 10
used = [0] * N
perm(0, 10)