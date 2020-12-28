# front,rear 이용
size=4
Q=[0]*size
front,rear=0,0 #프론트 자리에는 값을 넣어주면 안된다. 꽉찼는지 아닌지 확인 하기 위해

def enQueue(item):
    global rear
    if (rear+1)%size == front: # full
        print("Queue Full")
    else:
        rear=(rear+1)%size
        Q[rear]=item

def deQueue():
    global front
    if front==rear:
        print("queue empty")
    else:
        front=(front+1)%size
        return Q[front]

def Qpeek():
    if front==rear:
        print('queue empty')
    else:
        return Q[(front+1) % size]


enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
enQueue(4)
print(deQueue())
enQueue(5)
print(deQueue())
print(Q)
