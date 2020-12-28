def check(x, y):
    for i in range(1, x+1):
        if x % i == 0 and y % i == 0:
            ans = i

    return ans


def check2(x, y):
    while y != 0:
        r = x% y
        x = y
        y = r

    return x


n, k = map(int, input().split())

gcd = check2(n, k) # 최대공약수
lcm = (n*k)//gcd # 최소공배수
# a * b = gcd * lcm

print(gcd)
print(lcm)