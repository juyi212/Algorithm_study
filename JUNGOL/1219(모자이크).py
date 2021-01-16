def need(width):
    # width 로 색종이를 덮을 수 있을지 없을지 확인
    prev = -1
    ret = 0
    for pos in arr:
        if prev == -1:
            # 처음에 시작점 지정
            prev = pos
            ret += 1
        elif prev + width <= pos:
            # 더했을때 pos 보다 작으면 시작점 변경 및 색종이 더해주기
            prev = pos
            ret += 1
    return ret


r, c = map(int, input().split()) # 행, 열
n = int(input()) #색종이 갯수
max_height = 0
arr = []

for i in range(int(input())):
    s, e = map(int, input().split())
    # 행에서 가장 긴 것 찾기
    max_height = max(max_height, s)
    arr.append(e) # 어차피 밑에선에 맞춰서 넣어야하기때문에 열만 저장
arr.sort() # 순차적으로


l = max_height
r = 1000000

while l < r:
    # 색종이 너비 이진탐색
    m = (l+r) // 2
    if need(m) <= n:
        # 갯수가 맞고 최소의 길이를 찾아야함
        r = m
    else:
        # 색종이 수가 더 많이 필요함
        l = m+1
print(r)

# 전체 길이 중에서 짧은 걸 기준으로
# 1cm 씩 줄여나가며 분할하여 체크하기..
# 위에는 고정으로 붙여져 있어야함.
# 겹치는 거 가능
# 골드 3 ㅠㅠ

#
# def func(mid):
#     cnt = 0
#     i = 1000001
#
#     for x, y in arr:
#         if x > mid:
#             return False
#         if i <= y < i + mid:
#             pass
#         else:
#             cnt += 1
#             i = y
#     return cnt <= n
#
#
# r, c = map(int, input().split())  # 행, 열
# n = int(input())  # 색종이 갯수
# arr = []
# for i in range(int(input())):
#     s, e = map(int, input().split())
#     arr.append([s, e])
# arr = sorted(arr, key=lambda x: x[1])
#
# a, b = 0, max(r, c)
# m = (a + b) // 2
# while a < m < b:
#     if func(m):
#         b = m
#     else:
#         a = m
#     m = (a + b) // 2
# print(m+1)
