def solution(A, B):
    A.sort()
    B.sort()
    j = 0
    cnt = 0
    # sort 한 다음 B가 큰것만 count 해주겠다는 것임
    for i in range(len(B)):
        if A[j] < B[i]:
            cnt += 1
            j += 1
    return cnt