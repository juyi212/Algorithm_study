import math

n = int(input())
sq = int(math.sqrt(n))  # 제곱근 까지
arr = [0] * 1000
cnt = 0

for i in range(1, sq+1):
    if n % i == 0:
        cnt += 1
        arr[cnt] = i    # 작은 수 저장
        if n//i != i:
            cnt += 1
            arr[cnt] = n//i # 큰 수 저장 # 2*12 = 24, 12 저장

arr.sort()
for i in arr:
    if i != 0:
        print(i, end = ' ')

