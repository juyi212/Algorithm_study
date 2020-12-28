# 거듭제곱 : 밑수와 제곱수를 입력받아서 결과를 반환하는 함수 작성
# 재귀는 기저부(가장 기본 단위 ) / 실행부 (재귀가 호출되는 일반적으로 연산이되는 부분)
def power(base,exponent):
    if exponent==0:
        return 1
    # exponent 제곱수가 짝수
    if exponent%2==0:
        new_base=power(base,exponent//2)
        return new_base * new_base

    # exponent 제곱수가 홀수
    if exponent%2==1:
        new_base = power(base, (exponent-1) // 2)
        return new_base*new_base*base

power(2,8) # 2의 8제곱을 구하라

