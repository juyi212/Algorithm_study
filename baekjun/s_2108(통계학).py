import sys

n = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for _ in range(n)]

print(round(sum(number) / n))
number.sort()
print(number[(n - 1) // 2])

cnt = {}
for num in number:
    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1

# x[1] 을 기준으로 내림차순, 같으면 x[0]은 오름차순
cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

if n > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# c = Counter(sorted(number))
# ans = c.most_common()   # 빈도 기준 내림차순
# ans = sorted(cnt.items(), key=lamda x: (-x[1], x[0]))
# 우선순위로 갯수는 내림차순, 숫자는 오름차순으로 정렬
#
# if n > 1:
#     if ans[0][1] == ans[1][1]:
#         print(ans[1][0])
#     else:
#         print(ans[0][0])
# else:
#     print(ans[0][0])

print(number[-1] - number[0])
