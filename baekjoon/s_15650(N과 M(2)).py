from itertools import combinations
# 조합

def comb(numbers):
    l = len(numbers)
    picked = []
    start = 1

    def recur(start, l):
        if len(picked) == m:
            print(*picked)
            return
        for i in range(start, n+1):
            picked.append(i)
            start = picked[-1] + 1
            recur(start, l)
            picked.pop()
    recur(start, l)


n, m = map(int, input().split())
numbers = [range(1, n + 1)]
comb(numbers)


# numbers = list(combinations(range(1, n+1),m))
#
# for num in numbers:
#     print(*num)