n = int(input())
arr = list()
hi = 666
cnt = 0
while True:
    if '666' in str(hi):
        cnt += 1
        if cnt == n:
            print(hi)
            break
    hi += 1

# 어떤 수에 6이 적어도 3개이상 연속이여야함

# while True:
#     string = str(hi)
#     if len(arr) == 10000:
#         break
#     if string.find('666') != -1:
#         # 666 이 없으면 -1 있으면 인덱스 출력해줌
#         if string not in arr: # 중복 제거
#             arr.append(string)
#     hi += 1 # 값을 하나씩 높여준다.
# print(arr[n-1])

