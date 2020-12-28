import sys
import math

# 이분탐색
def check():
    start = 0
    end = w
    while start <= end:
        mid = (start + end) // 2
        ans = math.trunc(100 * ((y+mid)/(x+mid)))
        if ans > z:
            end = mid - 1
        else:
            start = mid + 1

    print(end+1)

# 판 횟수가 올라갈 때, 이기는 횟수도 올라간다

x, y = map(int, sys.stdin.readline().split())   # 게임횟수, 이긴횟수
# trunc()함수는 내림을 하더라도 0으로 향하는 반면 floor() 함수는 무조건 아래만 향해 내림한다.

z = math.trunc(100*y/x) # 곱셈을 먼저해줘야함
# print(100*29/50)
# print(100*(29/50))

w = 1000000000

if z >= 99: # 절대 변하지 않을 수
    print(-1)
else:
    check()


# 수학식으로 풀 기  ~~~~ ceil(((z+1)*x - 100 * y) / (100-(z+1))) ceil 은 소수점 버리는 함수  마지막에



'''
50 29
2

1000000000 980000000

'''