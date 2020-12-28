def check_blank(string):
    for i in range(len(string)):
        if string[i] == '{' or string[i] == '(':
            check.append(string[i])
        elif string[i] == '}' or string[i] == ')':
            if len(check) == 0:
                return 0
            tmp=check.pop()
            if string[i]=='}' and tmp=='{':
                continue
            if string[i]==')' and tmp=='(':
                continue
            return 0
    if len(check) !=0:
        return 0
    return 1

t=int(input())
for tc in range(1,t+1):
    string=input()
    check=[]
    print(f'#{tc} {check_blank(string)}')