import sys
import math

N, L, W, H = map(int, sys.stdin.readline().split())

start = 0
# 길이 중에서 가장 긴 것으로 잡고
end = max(L, max(W, H))

# # 이진탐색
# for i in range(10000):
#     mid = (start + end) / 2
#     # 부피를 구할 때 몫으로
#     f = (L//mid) * (W//mid) * (H//mid)
#     if f >= N:
#         start = mid
#     else:
#         end = mid


end = min(L, W, H)
# while 문도 사용 가능
while not math.isclose(start, end):
    mid = (start + end) / 2
    # 부피를 구할 때 몫으로
    f = (L//mid) * (W//mid) * (H//mid)
    if f >= N:
        start = mid
    else:
        end = mid

print(start)

'''
1 1 1 8
'''
