# 중복 순열
# from itertools import product
#
# n, m = map(int, input().split())
# numbers = list(product(range(1, n+1), repeat=m))
#
# for num in numbers:
#     print(*num)


def n_perm(numbers):
    l = len(numbers)
    picked = []
    start = 1

    def recur(l):
        if len(picked) == m:
            print(*picked)
            return
        for i in range(1, n+1):
            picked.append(i)
            # start = picked[-1] + 1
            recur(l)
            picked.pop()
    recur(l)


n, m = map(int, input().split())
numbers = [range(1, n + 1)]
n_perm(numbers)
