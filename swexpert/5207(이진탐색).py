
# def check(l, r, value): # 이진탐색
#     global cnt
#     m = (l+r)//2
#
#     if n_arr[m] == value:
#         cnt += 1
#         return
#     elif l <= r:
#         if value < n_arr[m]:
#             check(l, m-1, value)
#         if n_arr[m] < value:
#             check(m+1, r, value)
#     else:
#         return

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    cnt = 0
    n_arr.sort()
    for value in m_arr:
        # 양방향으로 체크가된 수를 출력
        left = 0
        right = len(n_arr)-1
        f = 0
        while left <= right:
            m = (left + right)//2
            if n_arr[m] == value:
                cnt += 1
                break
            elif n_arr[m] > value:
                if f == 1:  # 왼쪽으로만 갔다는 의미
                    break
                right = m - 1
                f = 1
            else:
                if f == -1: # 오른쪽으로만 갔다는 의미
                    break
                left = m + 1
                f = -1
    print('#{} {}'.format(tc, cnt))