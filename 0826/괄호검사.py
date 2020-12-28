# 괄호가 정상적이면 t, 아니면 f
# target : 괄호 검사 대상 문자열
def check_bracket(target):
    # 여는 괄호가 나오면, stack 에 push
    # 닫는 괄호가 나오면, stack에서 pop
    # 문장이 끝났을 때, stack 이 비어 있으면 정상적인 괄호
    # 아니라면 비정상적인 괄호

    stack= list()
    for i in range(len(target)):
        if target[i]=="(" or target[i]== "[" or target[i]=="{":
            stack.append(target[i])
        elif target[i]==")"or target[i]== "]" or target[i]=="}":
            if len(stack)==0:
                return False
            tmp = stack.pop() #비어있지 않으면 pop하고, 짝이 맞는지 검사해줘야함.
            if target[i]==")" and tmp=="(":
                continue
            elif target[i] == "}" and tmp == "{":
                continue
            elif target[i]=="]" and tmp=="[":
                continue
            #여기까지 오면 스택은 비어 있지 않은데, 짝이 맞지 않음
            return False
    # 문자가 여는 괄호라면 push
    # 닫는 괄호면 pop, pop했는데 비어 있으면 f
    if len(stack) != 0:
        return False
    return True

# 반복문이 끝났을 때 stack이 비어 있으면 t
# 아니면 f
str="[({()()()})]"
print(check_bracket(str))