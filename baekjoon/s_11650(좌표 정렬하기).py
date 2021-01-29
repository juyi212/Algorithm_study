numbers = [list(map(int, input().split())) for _ in range(int(input()))]
numbers.sort(key=lambda x: (x[0], x[1])) # x를 기준으로 증가후, 같으면 뒤에걸 기준으로
for num in numbers:
    print(*num)