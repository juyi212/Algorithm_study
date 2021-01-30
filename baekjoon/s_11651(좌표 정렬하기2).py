numbers = [list(map(int, input().split())) for _ in range(int(input()))]
numbers.sort(key = lambda x: (x[1], x[0]))

for num in numbers:
    print(*num)