# 최적화 문제를 해결하는 알고리즘, 답이 여러 개 있을 때 제일 좋은거 또는
# 나쁜 것을 구하는 문제를 해결할 때 자주 쓰임
# 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여
# 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

#반복적 구조로 DP를 구현한 것임
def dp_fibo(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(dp_fibo(1000))


