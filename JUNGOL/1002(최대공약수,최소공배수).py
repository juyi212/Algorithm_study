def check(x, y):
    for i in range(1, y+1):
        if x % i == 0 and y % i == 0:
            ans = i
    return ans


n = int(input())
a = list(map(int, input().split()))

gcd = lcm = a[0]
for i in range(len(a)):
    gcd = check(gcd, a[i]) # 유클리드 호제법 이용
    lcm = (lcm * a[i])//check(lcm, a[i])

print(gcd, end = ' ')
print(lcm)