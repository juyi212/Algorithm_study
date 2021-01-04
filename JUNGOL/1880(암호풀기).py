code = list(input().rstrip())
sen = input()

total = ''
for i in range(len(sen)):
    a = ord(sen[i])
    if 65 <= a <= 90: # 대문자일 경우
        # upper 도 사용가능
        total += code[ord(sen[i]) - 65].upper()
    elif sen[i] == ' ':
        total += sen[i]
    elif 97 <= a <= 122:
        total += code[ord(sen[i]) - 97]
print(total)