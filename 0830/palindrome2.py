import sys
sys.stdin=open("pal_input.txt","r")
def check(m):
    global zwords
    for i in range(100):
        for j in range(100-m+1):
            temp=words[i][j:j+m]
            c_temp=zwords[i][j:j+m]
            if temp==temp[::-1] or c_temp==c_temp[::-1]:
                return True
    return False
for tc in range(1,11):
    t=int(input())
    words=[list(input().rstrip()) for _ in range(100)]
    zwords=list(zip(*words))
    for i in range(100,0,-1):
        if check(i): # 제일 긴 것을 구하는 것이기때문에 가장 긴 순으로 문자열의 길이를 설정해줌
            result=i
            break
    print(result)
