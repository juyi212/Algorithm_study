def f(n, s, N, r):  # 조합의 인덱스, 선택구간의 시작, 주어진 개수, 고를 개수
    if n == r:
        print(c)
    else:
        for i in range(s, N-r+n+1):
            c[n] = i
            f(n+1, i+1, N, r)


N = 10
r = 3
c = [0] * 3
f(0, 0, N, r)
