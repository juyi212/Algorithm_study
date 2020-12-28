t=int(input())
for tc in range(1,t+1):
    S=input()
    result=set()
    li_result=[]
    dic = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    for k in range(0,len(S),3):
        r=S[k:k+3]
        result.add(r)
        li_result.append(r)
    if len(li_result) != len(result):
        print(f'#{tc} ERROR')
    else:
        for i in li_result:
            dic[i[0]]-= 1
        print(f'#{tc}',end=' ')
        print(*dic.values())

'''

3
S01D02H03H04
H02H10S11H02
S10D10H10C01  
'''