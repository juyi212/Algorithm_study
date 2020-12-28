def inspection(string):
    stack=[]
    global count
    for st in string:
        if st=='{' or st=='(':
            stack.append(st)
        elif st=='}'or st==')':
            v=stack.pop()
            if v=='{' and st=='}':
                continue
            elif v=='(' and st==')':
                continue
    if len(stack)>0:
        return 0

    return 1

t=int(input())
for tc in range(1,t+1):
    string=input()
    count=0
    print(f'#{tc} {inspection(string)}')