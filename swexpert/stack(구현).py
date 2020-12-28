# class Stack:
#     #요소의 최대 개수가 정해져있는 stack 만들기
#     # 스택은 top+1위치에 데이터 추가,(push)
#     # top의 위치에 있는 데이터를 반환/삭제(pop)
#     def __init__(self,n):
#         self.top = -1   #초기 값은 데이터가 비어있으니 -1
#         self.s = [0] * n
#     def push(self,d): # top + 1에 데이터를 추가
#         # if self.top == len(self.s)-1:
#         #     return False
#         self.s[self.top+1] = d
#         self.top += 1
#         # return True
#     def pop(self):  # top에 위치한 원소를 반환/삭제
#         # return self.s[self.top]
#         if self.top == -1:
#             return None
#         value = self.s[self.top]
#         self.s[self.top] = 0
#         self.top -= 1
#         return value


class Stack:
    def __init__(self, n):
        self.top = -1
        self.s = [0] * n

    def push(self, d):
        self.s[self.top+1] = d
        self.top += 1


    def pop(self):
        if self.top == -1:
            return None
        value = self.s[self.top]
        self.s[self.top] = 0
        self.top -= 1
        return value


def dfs(v):
    my_stack = Stack(8)
    my_stack.push(v)
    while my_stack:
        v = my_stack.pop()
        if not v:
            return
        if v not in visited:
            visited.append(v)

        for w in arr[v]:
            if w not in visited:
                my_stack.push(w)


matrix = list(map(int, input().split()))
arr = [[] for _ in range(8)]

for i in range(8):
    s, e = matrix[i*2], matrix[(i*2)+1]
    arr[s].append(e)
    arr[e].append(s)
visited = []
dfs(1)
print(*visited)


'''
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''



# my_stack = Stack(5)
# my_stack.push(5)
# my_stack.push(4)
# my_stack.push(3)
# my_stack.push(2)
# my_stack.push(1)
# print(my_stack.pop())
# my_stack.push(1)
# print(my_stack.pop())
# my_stack.push(1)
# print(my_stack.pop())
