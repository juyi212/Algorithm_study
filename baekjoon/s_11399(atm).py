
n = int(input())
orders= list(map(int, input().split()))
orders.sort()
result = []
total = 0
for i in orders:
    result.append(i)
    total += sum(result[::])
print(total)