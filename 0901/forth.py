def check():
    stack=[]
    for i in board:
        if i =='.':
            if len(stack)>1:
                return f'error'
            a= stack.pop()
            return a
        elif i == '*':
            if len(stack)<2:
                return f'error'
            s1=stack.pop()
            s2=stack.pop()
            stack.append(s2*s1)
        elif i == '+':
            if len(stack)<2:
                return f'error'
            s1=stack.pop()
            s2=stack.pop()
            stack.append(s2+s1)
        elif i == '-':
            if len(stack)<2:
                return f'error'
            s1=stack.pop()
            s2=stack.pop()
            stack.append(s2-s1)
        elif i == '/':
            if len(stack)<2:
                return f'error'
            s1=stack.pop()
            s2=stack.pop()
            stack.append(s2//s1)
        else:
            stack.append(int(i))

t=int(input())
for tc in range(1,t+1):
    board=list(input().split())
    print(f'#{tc} {check()}')
'''
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
'''