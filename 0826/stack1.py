stack=[]

def push (item):
    stack.append(item)


def pop():
    if len(stack) == 0 :
        print("stack is empty")
        return
    else:
        return stack.pop()

push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())

# stack.append(1) push
# if stack:  # len(stack) !=0
    # print(stack.pop())