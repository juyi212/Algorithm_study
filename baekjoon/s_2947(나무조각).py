# 시뮬레이션 , 구현 문제

numbers = list(map(int, input().split()))

for i in range(1, len(numbers)):    # 1단계로 돌아가라 ! 입력받은 것이 아니고 바뀌고 첫번째
    for j in range(len(numbers)-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            print(*numbers)