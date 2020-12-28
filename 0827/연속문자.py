
t=int(input())
for tc in range(1,t+1):
    string=list(input())
    check=[]

    for i in range(len(string)):
        if len(check)==0:
            check.append(string[i])

        elif len(check)>0:
            if check[-1] == string[i]:
                check.pop()
            else:
                check.append(string[i])
    print(f'#{tc} {len(check)}')



'''
ABCCB
'''

# for ch in arr:
#     if not S:
#         S.append(ch)
#     elif ch!=S[-1]:
#         S.append(ch)
#     else:
#         S.pop()
#     print(len(S))
#
# for ch in arr:
#     if not S or ch!=S[-1]:
#         S.append(ch)
#     else:
#         S.pop()
#     print(len(S))