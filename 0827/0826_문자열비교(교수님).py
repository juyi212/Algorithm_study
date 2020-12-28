T=int(input())
for tc in range(1,T+1):
    result=0
    str1=input()
    str2=input()

    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                break
        else: #걸리지 않으면 문자열 존재
            result=1
            break
    print(f'{tc} {result}')