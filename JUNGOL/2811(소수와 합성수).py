
def check(n):
    # int sq = sqrt(n)라고 할 때, (i <= n / i)는 결과적으로 (i <= sq) 와 같다.
    # 1/10000로 단축

    j = 2
    while j <= n//j:
        if n % j == 0:
            return False
            break
        j += 1
    return True


number = list(map(int, input().split()))

for i in number:
    if i < 2:
        print('number one')
    else:
        if check(i):
            print('prime number')
        else:
            print('composite number')