import sys, math
from decimal import Decimal


N, K = map(int, sys.stdin.readline().split())
dolls = list(map(int, sys.stdin.readline().split()))
sum_s = [0] * (N+1)
st_s = [0] * (N+1)

# O(N^2)로 풀어야함
# 부분합
# float 연산일때는 Decimal 을 써줘야함 정확한 답을 위해
for i in range(1, N+1):
    sum_s[i] = sum_s[i-1] + dolls[i-1]
    st_s[i] = st_s[i-1] + dolls[i-1] ** 2

# 분산 = E(X^2) - (E(X))^2
min_v = 100000000000000
for i in range(K, N+1):     # K 이상
    for j in range(N-i+1):  # 1개씩 증가
        av = Decimal(sum_s[i+j] - sum_s[j]) / i
        st = Decimal(st_s[i+j] - st_s[j]) / i - av*av
        min_v = min(min_v, st)
print(min_v.sqrt())