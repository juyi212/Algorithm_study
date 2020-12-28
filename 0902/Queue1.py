# front,rear 이용
# queue는 맨앞에것을 삭제하면 인덱스도 옮겨줘야한다.

Q=[0]*100
front,rear=-1,-1 #원형 큐의 구조에서는 0,0 으로 초기화

def enQueue(item):
    global rear
    if rear == len(Q)-1:
        print("Queue Full")
    else:
        rear=rear+1
        Q[rear]=item

def deQueue():
    global front
    if front==rear:
        print("queue empty")
    else:
        front+=1
        return Q[front]


enQueue(1)
enQueue(2)
enQueue(3) # queue 선입선출
print(deQueue())
#-----------------------------
 #
 # Q.append(3) # enQueue
 # Q.pop(0) # deQueue 벗 실행이 조금 느림.