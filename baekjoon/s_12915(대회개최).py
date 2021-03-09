import sys

# def is_possible(e, em, m, mh, h, num):
#     e -= num
#     m -= num
#     h -= num
#     if e < 0:
#         e += em
#         if e < 0:
#             return False
#
#     if m < 0:
#         m += em
#         if m < 0:
#             m += mh
#             if m < 0:
#                 return False
#             else: # ??
#                 mh = m
#
#     if h <0:
#         h += mh
#         if h < 0:
#             return False
#     return True
#
#
# e, em, m, mh, h = list(map(int, sys.stdin.readline().rsplit()))
# # 이분 탐색
# # 개최할 수 있는 숫자를 정하고 Check
# left, right = 0, 10**7
# while left <= right:
#     mid = (left+right)//2
#     if is_possible(e, em, m, mh, h, mid):
#         left = mid + 1
#     else:
#         right = mid -1
# print(right)


E, EM, M, MH, H = map(int, sys.stdin.readline().rsplit())

e = E + EM
m = M
h = MH + H

# 한 곳에 다 넣고
# 모든 상황들을 생각해준다.
while True:
    min_v = min(e, m, h)
    if min_v == e:
        break
    elif min_v == h:
        break
    # 중간이 가장 작은 것은 상황이 다름.
    # em, hm 으로부터 받아올 수 있기 때문
    elif min_v == m:
        if e >= h:
            if e == E:
                if h == H:
                    # em, hm 0 => m 이 가장 작은 거
                    break
                else:
                    h -= 1
                    m += 1
            else:
                e -= 1
                m += 1
        else:
            if h == H:
                if e == E:
                    break
                else:
                    e -= 1
                    m += 1
            else:
                h -= 1
                m += 1
print(min(e, m, h))
