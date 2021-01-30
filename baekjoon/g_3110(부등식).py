import sys

# 메모리초과, 시간초과
# 중간값을 기준으로 풀어야함
n, m, z = map(int, sys.stdin.readline().split())

s1, s2 = map(int, sys.stdin.readline().split())
s = s1/s2
start = (s1 * m) /s2

e1, e2 = map(int, sys.stdin.readline().split())
e = e1/e2
end = (e1 * m) /e2

ns = (s1 * n) /s2

cnt = 0

ns = (s1 * n)/s2
ze = (e1 * z)/e2
for i in range(int(start), int(end)+1):
    mid = i/m
    nm = (i * n)/m
    if s < mid < e:
        for j in range(int(ns), int(nm)+1):
            if s < j/n < mid:
                for p in range(int(nm), int(ze)+1):
                    if mid < p/z < e:
                        cnt += 1

print(cnt)



'''
1 9 7
14 5
10 3
'''