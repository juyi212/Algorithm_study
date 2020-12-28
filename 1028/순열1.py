def perm(n, k):     # n 숫자를 결정할 인덱스, (결정한 개수) k 순열의 길이
    if n == k:
        print(a)
    else:
        for i in range(n, k):
            a[n], a[i] = a[i], a[n]     # 현재 숫자 유지부터, 오른쪽 끝까지 교환
            perm(n+1, k)        # 다음 자리 결정하러 이동 (n개 결정)
            a[n], a[i] = a[i], a[n]     # 교환적으로 복구




a = [1, 2, 3]
perm(0, 3)