
n = int(input())
m = int(input())

total = []
if n == 1:
    n = 2
for i in range(n, m+1):
    j = 2
    ch = False
    while j <= i//j:    # 제곱근으로 처리
        if i % j == 0:
            ch = True
            break
        j += 1
    if not ch:
        total.append(i)

if total:
    print(sum(total))
    print(min(total))
else:
    print('-1')