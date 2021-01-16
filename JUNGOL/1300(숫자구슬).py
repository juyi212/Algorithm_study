def check(cnt, s, e, group):
    global here
    if group < 1:
        return

    if s + cnt >= e:
        max_v = -1
        v = max(here)
        print(here)
        li = []
        for vv, c in here:
            li.append(c)
        li.append(v)
        total.append(li)
        here = []
        return

    value = 0
    for i in range(s, s+cnt):
        value += marbles[i]

    here.append([value, cnt])

    check(cnt+1, s+cnt, e, group-1)



N, M = map(int, input().split()) # 구슬 개수, 그룹의 수
marbles = list(map(int, input().split()))

here = []
total = []
check(2, 0, len(marbles), M)
print(total)

