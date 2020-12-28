#원소수가 3개인 부분집합을 생성
#1이 3개인 6자리 2진수가 있다면 --> 0도 3개

cards=[5,4,1,2,3,6]
cards.sort()
for subset in range(1<<6): #6자리
    A,B=[],[]
    #각자리 값을 확인
    for i in range(6): #2의 0승부터 5승까지 확인
        if subset&(1<<i): #1일경우
            A.append(cards[i])
        else: #0일 경우
            B.append(cards[i])
    if len(A) == len(B):
        print(A,B) #6C3 X 3C3 = 20X1 =20가지 중복 포함됨.

# 다시 봐야함.