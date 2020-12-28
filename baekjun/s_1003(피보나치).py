import sys


def check(n):
    if n < 2:
        return

    for i in range(2, n+1):
        zero.append(zero[i-2]+zero[i-1])
        one.append(one[i - 2] + one[i - 1])


for _ in range(int(sys.stdin.readline())):
    zero = [1, 0] # f(3) 일경우는 f1 f2가 포함되어 있음. 그래서 하나씩 더 해준다.
    one = [0, 1]
    n = int(sys.stdin.readline())
    check(n)
    print(zero[n], end =' ')
    print(one[n])
