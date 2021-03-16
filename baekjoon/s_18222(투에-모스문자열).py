
# 맨 처음에 0으로 시작
# 분할 정복
# 충분히 큰 n에 대해 2^n 길이의 문자열에서 시작해서, 반으로 나눠가며 왼쪽에 위치하면 반전 x
# 오른쪽에 위치하면 반전 0
# 이걸 비트로 표현하면 비트가 1 인것마다 반전이 생기는 것이기 때문에 반전한 횟수를 카운트
# 즉, 오른쪽을 기준으로 바뀐 것 횟수를 카운트 한다
# 시작은 0부터 이기때문에 홀수면 0 짝수면 1

def getIdx(num):
    v = 1
    while v*2 < num:
        v *= 2
    return num - v

k = int(input())
cnt = 0
while k != 0:
    cnt += 1
    k = getIdx(k)

if cnt % 2 == 1:
    print(0)
else:
    print(1)