def fibo(n):
    if n>=2 and len(memo) <=n:
        memo.append(fibo(n-1)+fibo(n-2))
    return memo[n]

memo=[0,1] # 참조형(RW)
print(fibo(100))
#재귀적 구조로 DP를 구현한 것임
#재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생