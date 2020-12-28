# 순열
# 행렬의 순서
arr=[1,2,3]
N=3
def perm(idx):
    # 현재 idx에서 해야할 모든 경우의 수
    # 나보다 뒤쪽에 있는 모든 요소들과 자리 바꾸기
    if idx>=N:
        print(arr)
        return

    for i in range(idx,N):  # 맨처음에는 자기자신과 자리를 바꾼다,
        arr[i],arr[idx]=arr[idx],arr[i]
        perm(idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]


perm(0)