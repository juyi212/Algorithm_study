import math

def solution(w, h):
    # 규칙 찾는 것 중요
    # 가로 세로 길이의 공약수가 존재하는 것을 인지 해야함
    # 있던 없던 빼준다
    # 접점이 있는거 없는걸로 구분
    # gcd 함수 써도 됨
    # def check(n, m):
    #     for i in range(1, n+1):
    #         if n % i == 0 and m% i ==0 :
    #             ans = i
    #     return ans
    a = math.gcd(w, h)
    answer = (w*h) - (w+h-a)
    return answer