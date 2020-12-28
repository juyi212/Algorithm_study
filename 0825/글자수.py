def num(str1,str2):

    dic={}
    for k in range(len(str1)):
        count=str2.count(str1[k])
        dic[str1[k]]=count

    return max(dic.values())

T=int(input())
for tc in range(1,T+1):
    str1,str2= [input() for _ in range(2)]
    print(f'#{tc} {num(str1,str2)}')