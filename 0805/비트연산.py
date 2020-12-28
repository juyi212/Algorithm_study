a=5 #0101
b=3 #0011
print(a & b) # 0001 논리곱
print(a | b) # 0111 논리합
print(1<<3) # 0001-> 1000
print(a ^ b) #0110 다르면 1

# i의 비트 0 0 0
# for i in range(1<<n): # 8번 반복
#     # i의 비트가 1인지 0인지 판단
#     for j in range(n):
#         #각각의 원소가 포함될지 안될지를 비트랑 비교
#         if i & (1<<j):~~~