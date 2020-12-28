# 최대 크기가 정해져있는 queue

class Queue:
    # 데이터를 뺄때는, front에서 빼고, 데이터를 추가할때는 rear에 추가
    def __init__(self, n):
        self.q = [0] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, d):
        self.rear += 1
        self.q[self.rear] = d

    def dequeue(self):
        self.front += 1
        return self.q[self.front]


# my_queue = Queue(10)
# my_queue.enqueue(5)
# my_queue.enqueue(4)
# my_queue.enqueue(3)
# my_queue.enqueue(2)
# my_queue.enqueue(1)
#
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())


def bfs(v):
    queue = []
    queue.append(v)

    while queue:
        v = queue.pop(0)

        if v not in visited:
            visited.append(v)

        for w in arr[v]:
            if w not in visited:
                queue.append(w)


matrix = list(map(int, input().split()))
arr = [[] for _ in range(8)]

for i in range(8):
    s, e = matrix[i*2], matrix[(i*2)+1]
    arr[s].append(e)
    arr[e].append(s)
visited = []
bfs(1)
print(*visited)


'''
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''