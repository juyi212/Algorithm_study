n = int(input())
number = list(map(int, input().split()))

# 앞에서부터 차근차근 하나씩 더함
max_s = -1
ans = 0
for i in range(n):
    ans += number[i]
    if max_s < ans:
        max_s = ans
    if ans < 0:
        ans = 0
print(max_s)