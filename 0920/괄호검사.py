t=int(input())

for tc in range(1,t+1):
    sentence=list(input())
    stack=[]
    count=0
    for i in range(len(sentence)):
        if sentence[i]=='(' or sentence[i]=='{':
            stack.append(sentence[i])
        elif sentence[i]==')'or sentence[i]=='}':
            if len(stack)!=0:
                a=stack.pop()
                if a=='(' and sentence[i]==')':
                    continue
                elif a=='{' and sentence[i]=='}':
                    continue
            else:
                stack.append(sentence[i])

    if len(stack)!=0:
        print(0)
    else:
        print(1)