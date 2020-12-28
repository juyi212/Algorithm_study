import sys
sys.stdin=open('cal_input.txt','r')

def rank(operator):
    if operator =='*':
        return 0
    elif operator=='+':
        return 1
    elif operator=='(' or operator==')':
        return 2
    else:
        return 3


def postfix_notation(cal_li):
    stack = []  # 연산자 임시 저장
    result = []  # 후위연산으로 바꾼 결과 저장
    for i in cal_li:

        # 숫자
        if i.isdecimal():
            # 그대로 출력
            result.append(i)

        # 연산자
        else:

            # 여는 괄호는 무조건 stack에 추가
            if i == '(':
                stack.append(i)

            elif stack and i == ')':

                # 닫는 괄호가 나오면 여는 괄호가 나올 때까지 stack을 모두 pop
                # 괄호 사이에 있는 연산들은 모두 괄호 안에서 처리되어야 하기 때문이다.
                # stack은 연산 우선순위 역순으로 정리되어 있기 때문에 pop()을 하면 연산 우선순위대로 나온다.
                while stack[-1]!='(':
                    result.append(stack.pop())
                stack.pop()
                    # 여는 괄호가 나오면 순회 종료
            else:
                # 스택이 비었으면 stack 추가
                if not stack:
                    stack.append(i)

                # 스택에 들어있는 연산자와 순위 비교
                else:

                    # 현재 연산자(i)가 stack에 들어있는 연산자보다 우선순위가 높으면, stack에 추가
                    if rank(i) < rank(stack[-1]):
                        stack.append(i)

                    # 우선순위가 같거나 낮으면, stack에 있는 연산자를 pop하고, 현재 연산자를 stack에 추가
                    else:
                        result.append(stack.pop())
                        stack.append(i)

    # stack에 남은 연산자 모두 출력
    for j in stack:
        result.append(stack.pop())
    print(result)
    return check(result)


def check(result):
    stack_r=[]
    for i in result:
        if i == '*':
            s1=stack_r.pop()
            s2=stack_r.pop()
            stack_r.append(s2*s1)
        elif i == '+':
            s1=stack_r.pop()
            s2=stack_r.pop()
            stack_r.append(s2+s1)
        elif i == '-':
            s1=stack_r.pop()
            s2=stack_r.pop()
            stack_r.append(s2-s1)
        elif i == '/':
            s1=stack_r.pop()
            s2=stack_r.pop()
            stack_r.append(s2//s1)
        else:
            stack_r.append(int(i))
    if len(stack_r):
        a=sum(stack_r)
        return a

for tc in range(1,11):
    n=int(input())
    cal_li=input()
    print(f'#{tc} {postfix_notation(cal_li)}')


