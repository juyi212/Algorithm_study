#힙은 완전 이진트리

tmp=[7,2,4,3,1,6,5]
size=len(tmp)
heap=[0]*128
heapcount=0 #현재 마지막 노드가 들어있는 인덱스
#최소힙 : 루트가 가장 작다
def heappush(value):
    global heapcount
    heapcount+=1
    heap[heapcount]=value
    #만약에 새롭게 정의된 자식이 부모노드보다 작으면,
    #부모노드와 위치를 바꿔줘야함
    cur=heapcount
    # 이진 트리를 배열로 표현할 때 부모노드의 인덱스는 (자식노드 인덱스)//2
    parent=cur//2

    # if heap[cur]<heap[parent]: #더 작은값이 올라가야함. 최소힙이라서
    #     heap[parent],heap[cur]=heap[cur],heap[parent]

    while parent>0 and heap[cur]<heap[parent]: #더 작은값이 올라가야함. 최소힙이라서
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent=cur//2

def heappop():
    global heapcount

    result=heap[1] #루트 노드를 없애기 전에 저장. 반환하기위해서

    #heap의 마지막 인덱스에 있는 노드를 root로 바꿔준다.
    heap[1]=heap[heapcount] #마지막노드를 가리키고 있음
    heap[heapcount]=0
    heapcount-=1 #마지막 노드 없어짐.
    parent=1
    child=parent*2 #부모와 위치를 바꿔줄 자식의 인덱스 인것임. 초기값을 왼쪽으로 잡아준 것임.
    # 오른쪽 자식이 있으면, 오른쪽이 작은지 왼쪽이 작은지 비교
    if child +1 <= heapcount:
        if heap[child] > heap[child+1]:
            child=child+1

    #만약에 자식과 부모노드 비교해서 자식노드가 더 작으면 바꿔줌
    while child<=heapcount and heap[parent]>heap[child]:
        heap[parent],heap[child]=heap[child],heap[parent]
        parent=child
        child=parent*2
        if child + 1 <= heapcount:
            if heap[child] > heap[child+1]:
                child = child + 1

    #자식들 중에서 작은 애가 부모가 되어야 함.
    return result

for i in tmp:
    heappush(i)
print(heap)

for i in range(len(tmp)):
    print(heappop(),end=' ')