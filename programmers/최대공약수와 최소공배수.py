def solution(n, m):
    def check(n, m):
        for i in range(1, n + 1):
            if n % i == 0 and m % i == 0:
                ans = i
        return ans



    a = check(n, m)
    b = (n * m) // a
    answer = [a, b]
    return answer

# 뉴클리드 호제법?
