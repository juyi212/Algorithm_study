def perm(n, k, m):  # n숫자를 결정할 자리 인덱스, k 순열의 길이, m 주어진 숫자의 개수
    if n == k:
        print(a[0:k])
    else:
        for i in range(n, m):   # n 번과 바꿀 위치
            a[n], a[i] = a[i], a[n]
            perm(n+1, k, m)
            a[n], a[i] = a[i], a[n]


a = [1, 2, 3, 4, 5]
perm(0, 4, 5)