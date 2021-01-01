n, m = map(int, input().split())

prime = [False] * 2000005
prime[0] = prime[1] = True

# 에라토스테네스의 채
for i in range(2, m+1):
    if i*i <= m:
        if not prime[i]:
            for j in range(i*i, m+1, i): # 숫자의 배수들을 다 1로 처 리
                prime[j] = True

cnt = 0
for i in range(n, m+1):
    if not prime[i]:   # 처리 안된 친구들만 더해준다
        cnt += 1
print(cnt)

# 시간초과
# cnt = 0
# for i in range(n, m+1):
#     j = 2
#     ch = False
#     while j <= i//j:
#         if i % j ==0:
#             ch = True
#             break
#         j += 1
#     if not ch:
#         cnt+= 1
#
# print(cnt)